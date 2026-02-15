def calculate_score(df):

    latest = df.iloc[-1]
    atr_mean = df["ATR"].mean()

    score = 0
    trend = "Neutral"

    if latest["EMA20"] > latest["EMA50"]:
        score += 30
        trend = "Bullish"

    if latest["RSI"] > 55:
        score += 20

    if latest["ATR"] > atr_mean:
        score += 20

    atr_percent = (latest["ATR"] / latest["Close"]) * 100
    stop_loss = round(atr_percent * 1.5, 2)
    target = round(stop_loss * 2, 2)

    return {
        "Score": score,
        "Trend": trend,
        "ATR%": round(atr_percent,2),
        "SL%": stop_loss,
        "Target%": target
    }
