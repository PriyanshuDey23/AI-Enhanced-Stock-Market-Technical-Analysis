import streamlit as st
import pandas as pd
import google.generativeai as genai
import plotly.graph_objects as go
import os
from Stock.helper import *
from dotenv import load_dotenv
from Stock.prompt import *

# Import and configure Generative AI model
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


# Set up Streamlit app
st.set_page_config(layout="wide", page_title="AI Stock Analysis", page_icon="📊")
st.markdown(
    """
    <style>
    .main { background: linear-gradient(to right, #1f4037, #99f2c8); color: white; }
    .sidebar .sidebar-content { background-color: #0e1117; }
    .sidebar .sidebar-content h2, .sidebar .sidebar-content label, .sidebar .sidebar-content div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📈 AI-Powered Technical Stock Analysis")
st.sidebar.header("Configuration 🛠️")

# Input for stock ticker and date range
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-14"))



# Fetch stock data if the button is clicked
if st.sidebar.button("Fetch Data"):
    st.session_state["stock_data"] = fetch_stock_data(ticker, start_date, end_date)
    st.success("Stock data loaded successfully!")

# Check if data is available
if "stock_data" in st.session_state:
    data = st.session_state["stock_data"]

    # Display stock data table
    with st.expander(f"📊 {ticker} Stock Data Table", expanded=True):
        st.dataframe(data)

    # Plot candlestick chart
    st.subheader("📉 Candlestick Chart with Technical Indicators")
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name="Candlestick"
    )])

    # Sidebar: Select technical indicators
    st.sidebar.subheader("Technical Indicators 📌")
    indicators = st.sidebar.multiselect(
        "Select Indicators:",
        ["20-Day SMA", "20-Day EMA", "20-Day Bollinger Bands", "VWAP"],
        default=["20-Day SMA"]
    )

    # Helper function to add indicators to the chart
    def add_indicator(indicator):
        if indicator == "20-Day SMA":
            sma = data['Close'].rolling(window=20).mean()
            fig.add_trace(go.Scatter(x=data.index, y=sma, mode='lines', name='SMA (20)'))
        elif indicator == "20-Day EMA":
            ema = data['Close'].ewm(span=20).mean()
            fig.add_trace(go.Scatter(x=data.index, y=ema, mode='lines', name='EMA (20)'))
        elif indicator == "20-Day Bollinger Bands":
            sma = data['Close'].rolling(window=20).mean()
            std = data['Close'].rolling(window=20).std()
            bb_upper = sma + 2 * std
            bb_lower = sma - 2 * std
            fig.add_trace(go.Scatter(x=data.index, y=bb_upper, mode='lines', name='BB Upper'))
            fig.add_trace(go.Scatter(x=data.index, y=bb_lower, mode='lines', name='BB Lower'))
        elif indicator == "VWAP":
            data['VWAP'] = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()
            fig.add_trace(go.Scatter(x=data.index, y=data['VWAP'], mode='lines', name='VWAP'))

    # Add selected indicators to the chart
    for indicator in indicators:
        add_indicator(indicator)

    # Update the chart layout and plot it
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig)

    # Sidebar: Display stock statistics
    st.sidebar.subheader("📈 **Stock Statistics**")
    st.sidebar.success(f"📈 **Max Price:** {data['Close'].max():,.2f} USD")
    st.sidebar.success(f"📉 **Min Price:** {data['Close'].min():,.2f} USD")
    st.sidebar.success(f"📊 **Mean Price:** {data['Close'].mean():,.2f} USD")
    st.sidebar.success(f"📈 **Standard Deviation:** {data['Close'].std():,.2f} USD")

    # Calculate and display growth
    growth = calculate_growth(data)
    if growth is not None:
        st.sidebar.success(f"🚀 **Growth in Period:** {growth:.2f}%")
    else:
        st.sidebar.write("**Growth in Period:** Data not available.")

    # Run AI analysis
    if st.button("Run AI Analysis"):
        with st.spinner("Analyzing the chart, please wait..."):
            try:
                # Generate a textual description of the chart and indicators
                description = describe_technical_indicators(data)

                # Prepare AI analysis prompt with the description
                prompt = PROMPT.format(description=description)  # Prompt imported


                model = genai.GenerativeModel(
                    model_name="gemini-2.0-flash",
                    generation_config={
                        "temperature": 1,
                        "top_p": 0.95,
                        "top_k": 40,
                        "max_output_tokens": 8192,
                    }
                )

                chat_session = model.start_chat(history=[])
                response = chat_session.send_message(prompt)

                # Display AI analysis result
                st.subheader("🧠 AI Analysis Results")
                response_text = response.text if hasattr(response, 'text') else "No valid response received."
                st.write(response_text)

            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
