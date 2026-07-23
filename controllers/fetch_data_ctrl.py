import sqlite3
from models.videos_model import VideoModel


def fetch_data_ctrl():
    try:
        response = VideoModel.fetch_all_data()
        return [dict(row) for row in response]

    except sqlite3.Error as e:
        print(e)
        return []