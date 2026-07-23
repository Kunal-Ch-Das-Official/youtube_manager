import sqlite3
from models.videos_model import VideoModel


def delete_one_ctrl(selected_video: dict):

    video_id = selected_video["id"]

    if not video_id:
        return "video id not exist in selected video."

    try:
        is_data_exist = VideoModel.fetch_single_data(video_id)

        if is_data_exist:
            remove_data = VideoModel.remove_one_video(video_id)
            if remove_data:
                return "Successfully removed"
            else:
                return "Unable to remove, try again."
        else:
            return "Something went wrong, data does not exist."
    except sqlite3.Error as error:
        print(error)
        return "Internal database error"
