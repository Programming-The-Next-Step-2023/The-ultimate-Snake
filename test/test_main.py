import unittest
import turtle
# local imports
import sys
sys.path.append(r"\Users\pia.koch\Documents\GitHub\My-App\The-ultimate-Snake")

from ..My_Snake_lib import game
from ..My_Snake_lib.game import up

obj = game.snake


# create test cases
# create class that inherits from unittest.testcases
class Testmoves(unittest.TestCase):
    
    # Test 1: snake.heading() != 270
    def test_up(self):
        obj.setheading(0)
        up()
        self.assertEqual(obj.setheading(), 90)
        # Test2: snake.heading() == 270
        obj.setheading(270)
        up()
        self.assertNotEqual(obj.setheading(),90)

'''
tests that if the snake is heading is not downwards (270), snake heading can go upwards (90)
when the Up-button is pressed on the keyboard, but cannot if heading is downwards.
'''

if __name__ == '__main__':
    unittest.main()
'''
to run, put this command in the terminal (and make sure you're in the test folder):
python -m unittest test_snake.py
'''