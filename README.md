
# AI-Powered Technical Stock Analysis

This web app allows you to perform technical stock analysis using AI. The app fetches stock data, visualizes it with candlestick charts, and applies various technical indicators like the 20-Day SMA, 20-Day EMA, Bollinger Bands, and VWAP. The AI model analyzes the chart and provides a buy/hold/sell recommendation based on the technical indicators and patterns.

## Features

- Input a stock ticker (e.g., AAPL, MSFT) and select a date range.
- Visualize the stock's historical data with a candlestick chart.
- Apply various technical indicators to the chart:
  - 20-Day Simple Moving Average (SMA)
  - 20-Day Exponential Moving Average (EMA)
  - 20-Day Bollinger Bands
  - Volume Weighted Average Price (VWAP)
- Run AI analysis to get a buy/hold/sell recommendation.
- View key stock statistics like max price, min price, mean price, and standard deviation.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/AI-Enhanced-Stock-Market-Technical-Analysis.git
   cd AI-Powered-Technical-Stock-Analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the Google API Key in .env
   ```bash
   GOOGLE_API_KEY="XXXXXXXX"
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Configuration

- **Stock Ticker**: Enter a stock ticker (e.g., AAPL, MSFT) to fetch the stock data.
- **Date Range**: Set the start and end dates for the stock data.

## Requirements

- Python 3.9+
- Streamlit
- yFinance
- Plotly
- Google Generative AI (for AI analysis)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
