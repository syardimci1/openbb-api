from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/price/{ticker}")
def get_price(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return {"ticker": ticker, "price": data["Close"].iloc[-1]}

@app.get("/health")
def health():
    return {"status": "ok"}