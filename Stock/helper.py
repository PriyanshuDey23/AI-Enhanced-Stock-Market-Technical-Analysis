import yfinance as yf

# Function to fetch stock data
def fetch_stock_data(ticker, start, end):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start, end=end)
    return data

# Function to calculate growth
def calculate_growth(data):
    if not data.empty:
        start_price = data['Close'].iloc[0]
        end_price = data['Close'].iloc[-1]
        growth = ((end_price - start_price) / start_price) * 100
        return growth
    return None

# Function to describe technical indicators
def describe_technical_indicators(data):
    description = []

    # 20-Day SMA and EMA crossover
    sma = data['Close'].rolling(window=20).mean()
    ema = data['Close'].ewm(span=20).mean()
    crossover = ""
    if sma.iloc[-2] < ema.iloc[-2] and sma.iloc[-1] > ema.iloc[-1]:
        crossover = "Bullish crossover (SMA crossed above EMA)"
    elif sma.iloc[-2] > ema.iloc[-2] and sma.iloc[-1] < ema.iloc[-1]:
        crossover = "Bearish crossover (EMA crossed above SMA)"
    
    description.append(f"SMA and EMA Crossover: {crossover}")

    # Bollinger Bands
    sma_20 = data['Close'].rolling(window=20).mean()
    std = data['Close'].rolling(window=20).std()
    bb_upper = sma_20 + 2 * std
    bb_lower = sma_20 - 2 * std
    bb_status = ""
    if data['Close'].iloc[-1] > bb_upper.iloc[-1]:
        bb_status = "Price breakout above the upper Bollinger Band (Bullish)"
    elif data['Close'].iloc[-1] < bb_lower.iloc[-1]:
        bb_status = "Price breakout below the lower Bollinger Band (Bearish)"
    else:
        bb_status = "Price is within the Bollinger Bands"
    
    description.append(f"Bollinger Bands Status: {bb_status}")

    # VWAP
    vwap = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()
    vwap_status = "Price is above the VWAP (Bullish)" if data['Close'].iloc[-1] > vwap.iloc[-1] else "Price is below the VWAP (Bearish)"
    description.append(f"VWAP Status: {vwap_status}")

    # Candlestick pattern (simplified for now)
    candlestick_patterns = []
    if data['Close'].iloc[-1] > data['Open'].iloc[-1]:
        candlestick_patterns.append("Bullish candlestick")
    elif data['Close'].iloc[-1] < data['Open'].iloc[-1]:
        candlestick_patterns.append("Bearish candlestick")
    else:
        candlestick_patterns.append("Doji candlestick")
    
    description.append(f"Candlestick Patterns: {', '.join(candlestick_patterns)}")

    return "\n".join(description)