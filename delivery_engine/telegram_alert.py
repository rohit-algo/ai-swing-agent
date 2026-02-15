import requests
from datetime import datetime

BOT_TOKEN = "8247610114:AAF72IHCPbpjbPqP35cXzdDTpWYHY5sfdYE"
CHAT_ID = "6427589060"

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        print("Telegram Error:", response.text)


def send_start_message():
    message = f"""
🤖 *NSE Quant Scanner Started*
⏰ {datetime.now().strftime('%d-%m-%Y %H:%M')}
━━━━━━━━━━━━━━━━━━━━
"""
    send_alert(message)
