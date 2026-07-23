import sqlite3
from config.storage_path import storage_path


DATABASE_NAME = storage_path()


def sqlite_config() -> sqlite3.Connection:
    """
    Creates and returns a SQLite database connection.
    """

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row

        # Enable foreign key support
        conn.execute("PRAGMA foreign_keys = ON")

        return conn

    except sqlite3.Error as e:
        raise RuntimeError(f"Unable to connect to database: {e}") from e