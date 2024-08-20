# Alpha Vantage API Integration

## Overview

This project is a Python application that connects to the Alpha Vantage API to fetch stock data and display it on a web page using Flask.

## Project Structure

- `main.py`: The main Python script that sets up the Flask application, fetches stock data from Alpha Vantage, and renders it on the DOM.
- `.env`: A file to store environment variables, including the Alpha Vantage API key.
- `venv/`: The virtual environment directory containing installed dependencies.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd alpha_vantage_api
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file**:
    ```bash
    echo "ALPHA_VANTAGE_API_KEY=your_api_key_here" > .env
    ```

5. **Run the application**:
    ```bash
    python main.py
    ```

6. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Dependencies

- `requests`: For making HTTP requests to the Alpha Vantage API.
- `python-dotenv`: For managing environment variables.
- `Flask`: For creating the web server and rendering the web page.

## License

This project is licensed under the MIT License.