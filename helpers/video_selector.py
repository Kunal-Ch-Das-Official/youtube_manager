import curses


def video_selector(stdscr, videos, operation="Update"):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        if operation == "Update":
            stdscr.addstr(0, 0, "Select a video to update:\n")
        else:
            stdscr.addstr(0, 0, "Select a video to delete:\n")

        for index, video in enumerate(videos):
            text = f"{video['video_title']} ({video['duration']})"

            if index == current_row:
                stdscr.addstr(index + 2, 0, text, curses.A_REVERSE)
            else:
                stdscr.addstr(index + 2, 0, text)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(videos)
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(videos)
        elif key in (10, 13): 
            return videos[current_row]
