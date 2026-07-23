from pathlib import Path
from platformdirs import user_data_dir
from config.settings import APP_NAME, APP_AUTHOR

def storage_path():
    data_dir = Path(user_data_dir(APP_NAME, APP_AUTHOR))
    data_dir.mkdir(parents=True, exist_ok=True)

    db_path = data_dir / "youtube_videos.db"

    return db_path