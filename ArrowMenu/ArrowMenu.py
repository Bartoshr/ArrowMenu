import curses

class ArrowMenu():

    choosen_line = "{} {:>5}. {:<10}"
    normal_line = " {:>5}. {:<10} "

    def __init__(self, title, options=None,
                 arrow=">", search_enabled=False):
        if options is None:
            raise ValueError("Argument options is required")
        self.screen = None
        self.options = list(enumerate(options))
        self.search_enabled = search_enabled
        self.arrow = arrow
        self.title = title
        self.input = ""
        self.position = 0
        self.offset = 0
        self.limit = None

    def _courses_settings(self):
        self.screen = curses.initscr()
        if self.limit is None:
            self.limit = self.screen.getmaxyx()[0] - 5
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.screen.keypad(True)

    def _print_menu(self):
        self.screen.clear()
        print(self.screen.getmaxyx)
        f_options = self.filtered_options()
        f_options = f_options[self.offset: min(len(f_options), self.offset+self.limit)]
        options_len = len(f_options)
        self.screen.addstr(0, 0, self.title, curses.A_BOLD)
        for i, _ in enumerate(f_options):
            if self.position == i:
                self.screen.addstr(i + 2, 0, ArrowMenu.choosen_line.format(self.arrow, i + 1, f_options[i][1]))
            else:
                self.screen.addstr(i + 2, 0, ArrowMenu.normal_line.format(i + 1, f_options[i][1]))
        if self.search_enabled:
            self.screen.addstr(options_len + 3, 0,
                               "search: {}".format(self.input),
                               curses.A_UNDERLINE)

    def filtered_options(self):
        return list(filter(lambda x: self.input in x[1], self.options))

    def _on_key_up(self):
        f_options = self.filtered_options()
        len_options = len(f_options)
        if len_options < self.limit:
            self.position = (self.position - 1) % len_options
        elif len_options > self.limit and self.position != 0:
            self.position = (self.position - 1)
        elif len_options > self.limit and self.position == 0:
            self.offset = self.offset - 1 if self.offset - 1 > 0 else 0

    def _on_key_down(self):
        f_options = self.filtered_options()
        len_options = len(f_options)
        if len_options < self.limit:
            self.position = (self.position + 1) % len_options
        elif len_options > self.limit and self.position != self.limit-1:
            self.position = (self.position + 1)
        elif (len_options > self.limit and
              self.position == self.limit-1 and
              self.offset != len_options - self.limit):
            self.offset = self.offset + 1 if self.offset + 1 < len_options - 1 else len_options - 1

    def show(self):
        self._courses_settings()
        self._print_menu()
        try:
            while True:
                char = self.screen.getch()
                if char == ord("\n"):
                    return self.filtered_options()[self.position][0]
                elif char == 127:
                    self.input = self.input[:-1]
                    self.screen.clrtoeol()
                elif char == 27:
                    return None
                elif char == curses.KEY_UP:
                    self._on_key_up()
                elif char == curses.KEY_DOWN:
                    self._on_key_down()
                elif char < 255 and self.search_enabled:
                    self.input += chr(char)
                self._print_menu()
        finally:
            curses.nocbreak()
            self.screen.keypad(0)
            curses.echo()
            curses.endwin()

if __name__ == '__main__':
    choices = ["blue", "red"]
    menu = ArrowMenu("Which pill ?",
                     options=choices,
                     search_enabled=True)
    choosen = menu.show()
    if choosen:
        print("\nYou choose", choices[choosen], "\n")
    else:
        print("Exited")
