PROMPT = """

Based on the provided stock chart and technical indicators, analyze and provide a recommendation:
{description}

**Recommendation:** Provide a Buy, Hold, or Sell recommendation with detailed reasoning.

- **Candlestick Patterns**: Examine the price action and identify key candlestick patterns (e.g., hammer, doji, engulfing, shooting star). Highlight any significant reversal patterns, especially near key support or resistance levels.
- **Technical Indicators**:
- **20-Day Simple Moving Average (SMA)**: Assess the trend direction and look for crossovers (e.g., SMA crossing above the price for a bullish signal, or below for a bearish signal).
- **20-Day Exponential Moving Average (EMA)**: Evaluate its relationship with the 20-Day SMA. A crossover between these averages can signal a shift in market momentum.
- **Bollinger Bands**: Observe whether the price is bouncing within the bands or breaking above/below them. Pay attention to any squeezes indicating low volatility or breakouts signaling increased volatility.
- **Volume Weighted Average Price (VWAP)**: Determine if the price is above or below the VWAP. A price above VWAP typically indicates bullish sentiment, while a price below it indicates bearish sentiment.

Provide a detailed explanation of your recommendation based on the following:
- **Overall Trend**: Is the market in an uptrend, downtrend, or sideways?
- **Momentum**: Analyze the momentum based on the SMA/EMA relationship, as well as the behavior of the Bollinger Bands and VWAP.
- **Reversal Signals**: Identify any significant candlestick patterns that suggest a potential reversal or continuation.
- **Volume**: Consider the role of volume in confirming signals. Is the price movement supported by volume increases?

Ensure that your recommendation is based on the combination of these indicators and price action. Mention any key observations such as strong support or resistance levels, overbought or oversold conditions, and the overall market sentiment.

"""