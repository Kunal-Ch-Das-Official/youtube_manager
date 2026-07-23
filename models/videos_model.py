import uuid
from config.sqlite_config import sqlite_config


class VideoModel:
    @staticmethod
    def create_table():
        conn = sqlite_config()

        conn.execute("""
            CREATE TABLE IF NOT EXISTS youtube_videos (
                id TEXT PRIMARY KEY NOT NULL,
                video_title TEXT NOT NULL,
                duration TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()

    # Add new video to database
    @staticmethod
    def add_new_video(video_title: str, time_duration: str) -> str:
        conn = sqlite_config()

        video_id = str(uuid.uuid4())

        conn.execute(
            """
            INSERT INTO youtube_videos (id, video_title, duration)
            VALUES (?, ?, ?)
            """,
            (video_id, video_title, time_duration),
        )

        conn.commit()
        conn.close()

        return video_id

    # Update video in database
    @staticmethod
    def update_video(video_id: str, video_title: str, time_duration: str) -> bool:
        conn = sqlite_config()

        cursor = conn.execute(
            """
            UPDATE youtube_videos
            SET
                video_title = ?,
                duration = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (video_title, time_duration, video_id),
        )

        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()

        return updated

    # Fetch all videos
    @staticmethod
    def fetch_all_data():
        conn = sqlite_config()

        videos = conn.execute(
            "SELECT * FROM youtube_videos"
        ).fetchall()

        conn.close()

        return videos

    # Fetch a single video by ID
    @staticmethod
    def fetch_single_data(video_id: str):
        conn = sqlite_config()

        video = conn.execute(
            "SELECT * FROM youtube_videos WHERE id = ?",
            (video_id,),
        ).fetchone()

        conn.close()

        return video

    # Delete a video
    @staticmethod
    def remove_one_video(video_id: str) -> bool:
        conn = sqlite_config()

        cursor = conn.execute(
            "DELETE FROM youtube_videos WHERE id = ?",
            (video_id,),
        )

        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()

        return deleted