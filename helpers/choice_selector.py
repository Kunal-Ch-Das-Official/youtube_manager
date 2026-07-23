import curses


def choice_selector(stdscr, choices: list):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Please select an option:\n")

        for index, choice in enumerate(choices):

            if index == current_row:
                stdscr.addstr(index + 2, 0, choice, curses.A_REVERSE)
            else:
                stdscr.addstr(index + 2, 0, choice)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(choices)
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(choices)
        elif key in (10, 13, curses.KEY_ENTER):  # Enter
            return choices[current_row]
