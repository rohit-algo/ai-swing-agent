import numpy as np


def calculate_score(symbol, df):

    if df is None or df.empty or len(df) < 50:
        return None

    latest = df.iloc[-1]

    # ==============================
    # 🔍 SAFETY CHECK
    # ==============================

    required_cols = ["SMA20", "SMA50", "RSI", "ATR", "Close"]

    for col in required_cols:
        if col not in df.columns:
            print(f"Missing column: {col} in {symbol}")
            return None

    score = 0
    trend = "Neutral"

    # ==============================
    # 📈 TREND SCORE (30)
    # ==============================

    if latest["SMA20"] > latest["SMA50"]:
        score += 30
        trend = "Bullish"
    else:
        score += 10
        trend = "Bearish"

    # ==============================
    # ⚡ RSI MOMENTUM SCORE (30)
    # ==============================

    rsi = latest["RSI"]

    if 50 < rsi < 70:
        score += 30
    elif 40 <= rsi <= 50:
        score += 20
    elif rsi < 40:
        score += 10

    # ==============================
    # 💰 PRICE ABOVE SMA20 (20)
    # ==============================

    if latest["Close"] > latest["SMA20"]:
        score += 20

    # ==============================
    # 🔥 VOLATILITY CONFIRMATION (20)
    # ==============================

    if latest["ATR"] > df["ATR"].mean():
        score += 20

    # ==============================
    # 🧠 FINAL RETURN STRUCTURE
    # ==============================

    return {
        "Stock": symbol,
        "Score": int(score),
        "Trend": trend,
        "RSI": round(float(latest["RSI"]), 2),
        "ATR": round(float(latest["ATR"]), 2)
    }
