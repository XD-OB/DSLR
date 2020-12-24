import curses

menu = ['Start', 'Settings', 'Exit']
harry = [
    '                                         _ __',
    "        ___                             | '  \ ",
    "   ___  \ /  ___         ,'\_           | .-. \        /|",
    "   \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|",
    " _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _",
    "// | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_",
    "\\\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \ ",
    " `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|",
    "   | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |",
    "   | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |",
    "   /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |",
    "        /_\           `------'        \ |   AND        `.\  | |  `._,' /_\ ",
    "                                       \|       THE          `.\ ",
	"                  ___          _   _             _  _      _      ",
	"                 / __| ___ _ _| |_(_)_ _  __ _  | || |__ _| |_	   ",
	"                 \__ \/ _ \ '_|  _| | ' \/ _` | | __ / _` |  _|",
	"                 |___/\___/_|  \__|_|_||_\__, | |_||_\__,_|\__|",
	"                                         |___/                 ",
]

def print_menu(stdscr, selected_row_idx):
	stdscr.clear()
	h, w = stdscr.getmaxyx()
	maxlen = len(max(harry, key=len))
	for idx, row in enumerate(harry):
		x = w//2 - maxlen//2
		y = idx
		stdscr.addstr(y, x, row)
	for idx, row in enumerate(menu):
		x = w//2 - len(row)//2
		y = h//2 - len(menu)//2 + idx + 9
		if idx == selected_row_idx:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y, x, row)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y, x, row)
	stdscr.refresh()


def print_center(stdscr, text):
	stdscr.clear()
	h, w = stdscr.getmaxyx()
	x = w//2 - len(text)//2
	y = h//2
	stdscr.addstr(y, x, text)
	stdscr.refresh()


def main(stdscr):
	# turn off cursor blinking
	curses.curs_set(0)

	# color scheme for selected row
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# specify the current selected row
	current_row = 0

	# print the menu
	print_menu(stdscr, current_row)

	while 1:
		key = stdscr.getch()

		if key == curses.KEY_UP and current_row > 0:
			current_row -= 1
		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row += 1
		elif key == 10:
			print_center(stdscr, "You selected '{}'".format(menu[current_row]))
			stdscr.getch()
			# if user selected last row, exit the program
			if current_row == len(menu)-1:
				break

		print_menu(stdscr, current_row)


curses.wrapper(main)