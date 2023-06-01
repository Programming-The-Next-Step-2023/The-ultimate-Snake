from turtle import _Screen, Screen
#### create a very simple start game using the turtle module
import turtle
import time

### Create the screen
screen = turtle.Screen()
turtle.title("The ultimate Snake")

### create the snake 
snake = turtle.Turtle()
snake.color("green", "red")
snake.shape("turtle")
snake.shapesize(1,1,1)
snake.penup()
### color of the snake 
'''
let the player decide the color lateron; maybe also if they want to be a turtle or a snake
'''

### move the snake
snake.speed(2)
'''
the speed can be changed by writing the speed command in front of the moving command.
I want to increase speed with increased score.
'''
### define that snake cannot move in 180 degrees at once
def up():
    if snake.heading() !=270:
        snake.setheading(90)

def down():
    if snake.heading() != 90:
        snake.setheading(270)

def left():
    if snake.heading() != 0:
        snake.setheading(180)

def right():
    if snake.heading() != 180:
        snake.setheading(0)

'''
Example for the up function: If the up function is called, it checks whether the snake is not
currently heading downwards (270). If it is indeed not (i.e., it is heading left or right), 
up can be executed. The same principle applies for all 4 directions. 
'''

# call the screen to 'listen' to the keyboard
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

while True:
    snake.forward(2)


time.sleep(4)


### create borders