import unittest


import My_Snake_lib.game as g
from My_Snake_lib.game import up

### ModuleNotFoundError: No module named 'My_Snake_lib.game


# create test cases
# create class that inherits from unittest.testcases
class Testmoves(unittest.TestCase):
    
    # Test 1: snake.heading() != 270
    def test_up(self):
        '''
        Function that takes no arguments. It tests that the snake cannot head upwards when it is currently heading downwards. 
        '''
        g.snake.setheading(0)
        up()
        self.assertEqual(g.snake.setheading(), 90)
        # Test2: snake.heading() == 270
        g.snake.setheading(270)
        up()
        self.assertNotEqual(g.snake.setheading(),90)



if __name__ == '__main__':
    unittest.main()
'''
to run, put this command in the terminal (and make sure you're in the test folder):
python -m unittest test_game.py
'''
### ImportError: Failed to import test module: test_game