import ta

def add_technical_indicators(df):

    df["EMA20"] = df["Close"].ewm(span=20).mean()
    df["EMA50"] = df["Close"].ewm(span=50).mean()

    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()

    df["ATR"] = ta.volatility.AverageTrueRange(
        df["High"], df["Low"], df["Close"]
    ).average_true_range()

    return df
