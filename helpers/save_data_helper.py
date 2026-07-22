import json
import os
from config import DATA_FILE

def save_data_helper(videos):
    os.makedirs("data", exist_ok=True)


    with open(DATA_FILE, "w") as file:
        json.dump(videos, file)
