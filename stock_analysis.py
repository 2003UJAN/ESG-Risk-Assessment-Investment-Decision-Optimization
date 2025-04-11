import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")
    return df

def correlate_esg_stock(ticker, sentiment_score):
    df = get_stock_data(ticker)
    df["ESG Sentiment"] = sentiment_score  # Assume constant sentiment
    correlation = df["Close"].corr(pd.Series([sentiment_score] * len(df)))
    return correlation

# Example usage
ticker = "AAPL"
sentiment_score = 4.0  # Example score
correlation = correlate_esg_stock(ticker, sentiment_score)
print(f"Correlation between ESG sentiment & {ticker} stock: {correlation:.2f}")
