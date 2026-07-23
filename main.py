import curses
from handler.add_new_video import add_new_video
from handler.delete_video import delete_video
from handler.list_all_videos import list_all_videos
from handler.update_video import update_video
from helpers.load_data import load_data
from helpers.data_selector import data_selector


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager. | choose an option! ")
        print("Press (1) to list all youtube videos.")
        print("Press (2) for adding a new youtube video.")
        print("Press (3) to update a youtube video details.")
        print("Press (4) to delete a youtube video.")
        print("Press (5) for exist the app.")
        users_choice = int(input("Enter a value and press enter to continue...\n"))

        match users_choice:
            case 1:
                list_all_videos(videos)
                break
            case 2:
                add_new_video(videos)
                break
            case 3:
                selected_video = curses.wrapper(
                    data_selector, videos, operation="Update"
                )
                if selected_video:
                    update_video(selected_video, videos)
                break
            case 4:
                selected_video = curses.wrapper(
                    data_selector, videos, operation="Delete"
                )
                delete_video(selected_video, videos)
                break
            case 5:
                print("Thanks for visiting...")
                break
            case _:
                print("Invalid choice. Please enter a valid number")


# Function Calling 
if __name__ == "__main__":
    main()

