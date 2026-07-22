import json
from config import DATA_FILE

def delete_video(selected_video, videos):
    video_id = selected_video["id"]

    for video in videos:
        if video["id"] == video_id:
            videos.remove(video)
            break
    else:
        print("Video not found!")
        return

    with open(DATA_FILE, "w") as file:
        json.dump(videos, file, indent=4)

    print("Video deleted successfully!")