import json
from config import DATA_FILE
def update_video(selected_video: dict, videos):
    new_video_name = input("Enter new video name: ")
    new_duration = input("Enter the video duration: ")

    video_id = selected_video["id"]
    existing_name = selected_video["video_name"]
    existing_duration = selected_video["duration"]

    for video in videos:
        if video["id"] == video_id:

            if new_video_name == "":
                new_video_name = existing_name

            if new_duration == "":
                new_duration = existing_duration

            video["video_name"] = new_video_name
            video["duration"] = new_duration

            break
    else:
        print("Video not found!")
        return

    with open(DATA_FILE, "w") as file:
        json.dump(videos, file, indent=2)

    print("Video updated successfully!")