import json
import os
from config import DATA_FILE


def load_data():
    os.makedirs("data", exist_ok=True)

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError, json.JSONDecodeError:
        return []
