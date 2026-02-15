import yfinance as yf
import pandas as pd

def get_price_data(stock, period="6mo", interval="1d"):
    df = yf.download(stock, period=period, interval=interval, progress=False)

    if df.empty:
        return None

    # Fix MultiIndex if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df
