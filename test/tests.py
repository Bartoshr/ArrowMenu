from hecate.hecate import Runner
import sys
import os
sys.path.append(os.path.abspath('ArrowMenu'))
from ArrowMenu import ArrowMenu

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

def test_escape_exit():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        h.press("Escape")
        h.press("Escape")
        h.await_exit(timeout=5)

def test_long_cursor_down():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        for _ in range(30):
            h.press("Down")
        assert ">    19. 30" in h.screenshot()

def test_return_correct_first_value():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        h.press("Enter")
        assert "You choose 1" in h.screenshot()

def test_return_correct_last_value():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        for _ in range(30):
            h.press("Down")
        h.press("Enter")
        assert "You choose 30" in h.screenshot()

def test_search_after_moved_cursor_down():
    with Runner("python3", __file__) as h:
        h.await_text("Which pill ?")
        for _ in range(30):
            h.press("Down")
        h.press("1")
        assert "1. 1" in h.screenshot()


if __name__ == "__main__":
    choices = [str(i + 1) for i in range(30)]
    menu = ArrowMenu("Which pill ?",
                     options=choices,
                     search_enabled=True)
    choosen = menu.show()
    if choosen != None:
        print("\nYou choose", choices[choosen], "\n")
    else:
        print("Exited")
