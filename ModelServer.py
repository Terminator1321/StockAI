from flask import Flask, request, jsonify, render_template
import yfinance as yf
import pandas as pd
from tensorflow.keras.models import load_model
import joblib
import numpy as np
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")
CORS(app)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

tag_df = pd.read_csv("Stocks/clean_data/tag.csv")
features = ["Open", "High", "Low", "Close", "Volume", "CompanyID", "weekday", "year", "month", "day"]
model = load_model("Models/Stock_Predictor_v1.keras")
scalar = joblib.load("Models/scaler.pkl")

tag_data = {row['company tag']: row['CompanyID'] for _, row in tag_df.iterrows()}
tickers = tag_df['company tag'].tolist()
print(tag_data)
def get_day(date): return date.weekday() + 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api-key')
def get_api_key():
    if not RAPIDAPI_KEY:
        return jsonify({"error": "API key not configured"}), 500
    return jsonify({"key": RAPIDAPI_KEY})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ticker = request.json.get('ticker')
        end_date = pd.Timestamp.now() - pd.Timedelta(days=1)
        start_date = end_date - pd.Timedelta(days=60)
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date, interval="1d").fillna(0)
        df.reset_index(inplace=True)
        df['CompanyID'] = tag_data.get(ticker, 0)
        df['weekday'] = df['Date'].apply(get_day)
        df['year'] = pd.to_datetime(df['Date']).dt.year
        df['month'] = pd.to_datetime(df['Date']).dt.month
        df['day'] = pd.to_datetime(df['Date']).dt.day
        data = df[features]
        scaled = scalar.transform(data)
        X = np.array(scaled).reshape(1, scaled.shape[0], scaled.shape[1])
        pred_scaled = model.predict(X)
        placeholder = np.zeros((1, len(features)))
        placeholder[0, features.index("Close")] = pred_scaled[0, 0]
        pred_original = scalar.inverse_transform(placeholder)[0, features.index("Close")]
        return jsonify({"ticker": ticker, "predicted_close": round(float(pred_original), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
