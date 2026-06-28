import requests
from bs4 import BeautifulSoup
import json
import os

from retailers import RETAILERS
from config import KEYWORDS_IN_STOCK, PRODUCT_KEYWORDS, TIMEOUT
from notifier import send_email

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def is_in_stock(text):
    text = text.lower()
    return (
        any(k in text for k in KEYWORDS_IN_STOCK)
        and any(p in text for p in PRODUCT_KEYWORDS)
    )


def fetch(url):
    try:
        r = requests.get(url, timeout=TIMEOUT, headers={
            "User-Agent": "Mozilla/5.0"
        })
        return r.text.lower()
    except:
        return ""


def run():
    state = load_state()
    alerts = []

    for r in RETAILERS:
        text = fetch(r["url"])
        stock = is_in_stock(text)

        prev = state.get(r["name"], False)

        if stock and not prev:
            alerts.append(f"🔥 {r['name']} BACK IN STOCK!")

        state[r["name"]] = stock

    save_state(state)

    if alerts:
        send_email(
            "Midea PortaSplit Stock Alert",
            "\n".join(alerts)
        )


if __name__ == "__main__":
    run()
