import sqlite3
from models.videos_model import VideoModel


def add_new_data_ctrl(video_title: str, time_duration: str):
    try:
        response = VideoModel.add_new_video(video_title, time_duration)
        if not response:
            print("Something went wrong, please try again")
        else:
            print("Data added...")
    except sqlite3.Error as e:
        print(e)
