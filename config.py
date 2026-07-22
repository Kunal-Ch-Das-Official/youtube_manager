import os
import sys

if getattr(sys, "frozen", False):
    # Running as a PyInstaller executable
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Running as a Python script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "local_db.json")
