import streamlit as st
from esg_analysis import analyze_esg_sentiment
from stock_analysis import correlate_esg_stock

st.set_page_config(page_title="🌿 ESG Risk Assessment", layout="wide")

st.title("💹 ESG Risk Assessment & Investment Optimization 🚀")

uploaded_file = st.file_uploader("📂 Upload an ESG Report (TXT)", type="txt")

if uploaded_file is not None:
    # Read and analyze ESG report
    text = uploaded_file.read().decode("utf-8")
    sentiment = analyze_esg_sentiment(uploaded_file.name)
    
    st.subheader("📊 ESG Sentiment Analysis")
    st.write(sentiment)
    
    # Stock analysis
    ticker = st.text_input("📈 Enter Stock Ticker (e.g., AAPL, TSLA)")
    if ticker:
        correlation = correlate_esg_stock(ticker, sentiment[0]["score"])
        st.write(f"💰 ESG-Stock Correlation: **{correlation:.2f}**")
