import requests

from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(message, tg_chat_id):
    """Отправляет сообщение в Telegram по tg_chat_id."""
    params = {
        "text": message,
        "chat_id": tg_chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
