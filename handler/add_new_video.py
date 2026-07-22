import uuid
from helpers.save_data_helper import save_data_helper


def add_new_video(videos: list):
    video_name = input("Enter video name: \n")
    video_duration = input("Enter vide duration: \n")

    videos.append(
        {"id": str(uuid.uuid4()), "video_name": video_name, "duration": video_duration}
    )
    save_data_helper(videos=videos)
