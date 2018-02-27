import unittest
from menu import ArrowMenu

class TestMenu(unittest.TestCase):

    @unittest.expectedFailure
    def test_set_options_not_iterable(self):
        menu = ArrowMenu("Which pill ?")


if __name__ == '__main__':
    unittest.main()
