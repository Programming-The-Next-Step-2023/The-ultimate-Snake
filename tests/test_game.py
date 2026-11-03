import unittest

import My_Snake_lib.game as g


class FakeSnake:
    '''Stand-in for the turtle, so the tests run without opening a game window.'''

    def __init__(self, heading=0):
        self._heading = heading

    def heading(self):
        return self._heading

    def setheading(self, angle):
        self._heading = angle


class TestMoves(unittest.TestCase):

    def setUp(self):
        g.snake = FakeSnake()

    def test_up_when_heading_right(self):
        '''The snake can turn up when it is moving to the right.'''
        g.snake.setheading(0)
        g.up()
        self.assertEqual(g.snake.heading(), 90)

    def test_up_when_heading_down(self):
        '''The snake cannot turn up when it is moving down.'''
        g.snake.setheading(270)
        g.up()
        self.assertEqual(g.snake.heading(), 270)

    def test_down_when_heading_up(self):
        g.snake.setheading(90)
        g.down()
        self.assertEqual(g.snake.heading(), 90)

    def test_left_when_heading_right(self):
        g.snake.setheading(0)
        g.left()
        self.assertEqual(g.snake.heading(), 0)

    def test_right_when_heading_up(self):
        g.snake.setheading(90)
        g.right()
        self.assertEqual(g.snake.heading(), 0)


if __name__ == '__main__':
    unittest.main()

# Run from the main project folder (where setup.py is):
# python -m unittest discover tests
