# StockAI
A fun project combining AI and web dev to predict next-day stock prices. Built with Flask, TensorFlow, and Chart.js, it fetches live data via Yahoo Finance API and shows interactive charts with AI predictions for multiple companies. Made just for learning!

---

# 📈 StockAI — AI-Powered Stock Price Prediction

**StockAI** is a fun and educational project that combines **machine learning**, **data analysis**, and **web development** to predict next-day stock closing prices.
It’s designed purely for **learning purposes** and not for real trading.

---

## 🚀 Overview

The project tracks real-time stock data for multiple companies and uses a **pretrained deep learning model** to predict the next-day closing price.
It integrates a **Flask backend** (for prediction and API handling) with a **Chart.js frontend** that visualizes stock trends interactively.

---

## 🧠 Features

* Predicts **next-day closing prices** using a trained TensorFlow/Keras model
* Fetches **live 60-day stock data** using the Yahoo Finance API (via RapidAPI)
* Displays **interactive charts** with CSV download option
* Supports **15+ companies** (U.S. and Indian markets)
* Fully local — no cloud dependency

---

## 📁 Project Structure

📂 StockAI
┣ 📂 templates
┃ ┗ index.html → Frontend with Chart.js & AI output
┣ 📂 Models
┃ ┣ Stock_Predictor_v1.keras → Pretrained model
┃ ┗ scaler.pkl → Scaler used for normalization
┣ 📂 Stocks
┃ ┣ 📂 clean_data
┃ ┃ ┣ tag.csv
┃ ┃ ┗ combined_stock_data.csv
┣ train.ipynb → Model training notebook
┣ stocks_data_creator.ipynb → Data preprocessing script
┣ ModelServer.py → Flask backend API
┣ requirements.txt → Dependencies list
┗ .env (Not uploaded) → Contains your RAPIDAPI key

---

## ⚙️ Installation

1. Clone the repository:
   git clone [https://github.com/Terminator1321/StockAI.git](https://github.com/Terminator1321/StockAI.git)
   cd StockAI

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file in the project root and add your RapidAPI key:
   RAPIDAPI_KEY=your_api_key_here

4. Run the Flask server:
   python ModelServer.py

5. Open your browser and visit:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧩 Tech Stack

* Backend: Flask, TensorFlow/Keras, Pandas, yFinance
* Frontend: HTML, CSS, JavaScript (Chart.js)
* Data Source: Yahoo Finance API (via RapidAPI)

---

## ⚠️ Disclaimer

This project is **not intended for financial or investment advice**.
It’s made solely for **learning and experimentation** with AI and web development.

---

⭐ Made just for fun and learning — explore, modify, and experiment!

---

