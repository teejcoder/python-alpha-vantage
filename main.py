import os
import requests
from flask import Flask, render_template_string
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

app = Flask(__name__)

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

@app.route('/')
def home():
    return """
    <html>
      <head>
        <title>Stock App</title>
      </head>
      <body>
        <h1>Welcome to the Stock App!</h1>
        <p>This app retrieves stock data using the Alpha Vantage API.</p>
        <p>Click <a href="/api">here</a> to view the stock data.</p>
      </body>
    </html>
    """

@app.route('/api')
def index():
    symbol = 'AAPL'  # Example stock symbol
    data = get_stock_data(symbol)
    return render_template_string("""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Stock Data</title>
      </head>
      <body>
        <h1>Stock Data for {{ symbol }}</h1>
        <pre>{{ data | tojson(indent=2) }}</pre>
      </body>
    </html>
    """, symbol=symbol, data=data)

if __name__ == '__main__':
    app.run(debug=True)