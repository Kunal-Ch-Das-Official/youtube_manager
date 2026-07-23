import time
import curses
from models.videos_model import VideoModel
from controllers.fetch_data_ctrl import fetch_data_ctrl
from controllers.add_new_data_ctrl import add_new_data_ctrl
from controllers.update_one_ctrl import update_one_ctrl
from controllers.delete_one_ctrl import delete_one_ctrl

from helpers.choice_selector import choice_selector
from helpers.video_selector import video_selector


def main():

    VideoModel.create_table()

    choices = [
        "1. See all data",
        "2. Add a new data",
        "3. Update existing data",
        "4. Delete a data",
        "5. Exit program",
    ]

    while True:
        user_choice = curses.wrapper(choice_selector, choices)

        # todo: 1. Fetch all data from database .............
        if user_choice.startswith("1"):

            def fallback():
                print("Getting all data...\n")
                time.sleep(0.2)
                print("-" * 120)

            fallback()

            videos = fetch_data_ctrl()
            if len(videos) == 0:
                print("Please add a video first. No record found..")
                print("-" * 120)
            else:
                for video in videos:
                    print(video)
                    print("-" * 120)
                    print("\nSuccessful!")

        # * 2. Add new data to database..........
        elif user_choice.startswith("2"):
            video_title = input("Enter video title: \n")
            video_duration = input("Enter video duration: \n")

            if video_title == "" and video_duration == "":
                print("Please input value.")
            else:
                add_new_data_ctrl(video_title, video_duration)

        # ? 3. Update existing data from database ..........
        elif user_choice.startswith("3"):
            print("Updating data...")
            videos = fetch_data_ctrl()
            select_video = curses.wrapper(video_selector, videos, operation="Update")
            update_one_ctrl(selected_video=select_video)

        #! 4. Delete data from database ..........
        elif user_choice.startswith("4"):
            print("Deleting data...")
            videos = fetch_data_ctrl()
            select_video = curses.wrapper(video_selector, videos, operation="Delete")
            result = delete_one_ctrl(selected_video=select_video)
            print(result)

        #! 5. Exit the program..........
        elif user_choice.startswith("5"):
            print("Goodbye!")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
