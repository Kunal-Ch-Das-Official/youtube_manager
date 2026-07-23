import sqlite3
from models.videos_model import VideoModel


def update_one_ctrl(selected_video: dict):
    new_name = input("Please enter the video name: \n").strip()
    new_duration = input("Please enter duration: \n").strip()

    if not new_name:
        new_name = selected_video["video_title"]

    if not new_duration:
        new_duration = selected_video["duration"]

    try:
        updated = VideoModel.update_video(
            video_id=selected_video["id"],
            video_title=new_name,
            time_duration=new_duration,
        )

        if updated:
            print("Successfully updated!")
        else:
            print("Video not found!")

    except sqlite3.Error as e:
        print(e)