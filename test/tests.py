from hecate.hecate import Runner
import sys
import os
sys.path.append(os.path.abspath('./ArrowMenu'))
from menu import ArrowMenu

def test_move_cursor_down():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        h.press("Down")
        assert ">     2. 2" in h.screenshot()

def test_move_cursor_up():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        h.press("Down")
        h.press("Up")
        assert ">     1. 1" in h.screenshot()

def test_search_item():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        h.press("1")
        h.press("3")
        assert ">     1. 13" in h.screenshot()


if __name__ == "__main__":
    choices = [str(i + 1) for i in range(30)]
    menu = ArrowMenu("Which pill ?",
                     options=choices,
                     search_enabled=True)
    choosen = menu.show()
    print("\nYou choose", choices[choosen], "\n")
