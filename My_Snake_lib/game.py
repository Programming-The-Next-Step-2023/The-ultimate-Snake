#### create a very simple start game using the turtle module
import turtle
import time
import random 
from PIL import Image

### Create the screen
screen = turtle.Screen()
screen.title("The ultimate Snake")
screen.setup(width = 700, height = 700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")


### drawing borders
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-300,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()


# score
score = 0
delay = 0.1


### draw the snake 
snake = turtle.Turtle()
snake.speed()
snake.color("green", "red")
snake.shape("turtle") 
snake.shapesize(2,2,2)
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
# Register the image as a shape
sponge_b = "My_Snake_lib\Sponge1.gif"  # Replace with your image file name
# Resize the image
width, height = 30, 30  # Replace with your desired dimensions
sponge1 = Image.open(sponge_b)
resized_sponge1 = sponge1.resize((width, height))
resized_sponge1_path = "My_Snake_lib\small_Sponge_white.gif"  # Replace with the desired output file path
resized_sponge1.save(resized_sponge1_path)
screen.register_shape(resized_sponge1_path)

# create the food
food = turtle.Turtle()
food.speed(0)
food.shape(resized_sponge1_path)
food.penup()
food.goto(-50,50)
food.hideturtle()

# create the mating turtle
mate = turtle.Turtle()
mate.speed(0)
mate.shape("turtle")
mate.color("yellow", "blue")
mate.shapesize(2,2,2)
mate.penup()
mate.goto(-100,50)
mate.hideturtle()


# Variables
types = [food, mate] # list with both food and mate
current_food = random.choice(types)  # randomly select the between food and mate
current_food.showturtle()

# Initial turtle babies is an empty list
babies = []


# Score
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: ", align="center", font=("Courier", 24,"bold"))


def up():
    '''
    Function that takes no arguments. Checks that snake can only move in steps of 90 degrees.
    '''
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

    
# call the screen to 'listen' to the keyboard
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')



# main loop
while True:
    screen.update()
    

    # snake and food/mate collision
    if snake.distance(current_food) < 20:
        
        current_food.hideturtle()
        # create new random food/turtle
        x = random.randint(-260, 260)
        y = random.randint(-230, 230)

        # Set the new position for the next type
        new_food = random.choice(types)
        new_food.goto(x, y)

        
        if current_food == food:
            scoring.clear()
            score += 1
            scoring.write("Score: {}".format(score), align="center", font=("Courier", 24,"bold"))
            delay -= 0.01 # no endless reduction in delays / with new turtle delay increases again 

        elif current_food == mate:
            # create baby turtles
            baby = turtle.Turtle()
            baby.speed(0)
            baby.shape("turtle")
            baby.color("green", "red")
            baby.shapesize(1,1,1)
            baby.penup()
            babies.append(baby)

            delay += 0.005

        # set new_food back to current_food
        current_food = new_food
        current_food.showturtle()

        # Move each following baby to the position of the baby in front
    for i in range(len(babies) -1, 0, -1):
        heading = snake.heading()
        distance = 20
        if heading == 0: # moving right
            x = babies[i - 1].xcor() - distance
            y = babies[i - 1].ycor()  
        elif heading == 90: # moving up
            x = babies[i - 1].xcor() 
            y = babies[i - 1].ycor() - distance
        elif heading == 180: # moving left
            x = babies[i - 1].xcor() + distance
            y = babies[i - 1].ycor() 
        elif heading == 270: # moving down
            x = babies[i - 1].xcor() 
            y = babies[i - 1].ycor() + distance
        babies[i].goto(x, y)
    

    # Move the first baby to the position of the snake
    if len(babies) > 0: 
        heading = snake.heading()
        distance = 20
        if heading == 0: # moving right
            a = snake.xcor() - distance
            b = snake.ycor() 
        elif heading == 90: # moving up
            a = snake.xcor()
            b = snake.ycor() - distance
        elif heading == 180: # moving left
            a = snake.xcor() + distance
            b = snake.ycor() 
        elif heading == 270: # moving down
            a = snake.xcor() 
            b = snake.ycor() + distance
        babies[0].goto(a, b)

        

    # snake & border collision
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 230 or snake.ycor() < -230:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("blue")
        scoring.goto(0,0)
        scoring.write("   Game Over \n Your Score is {}".format(score),align="center", font=("Courier", 30,"bold"))
        break
    snake.forward(8)

    #check for collision with body
    for baby in babies:
        if baby.distance(snake)<10:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("blue")
            scoring.goto(0,0)
            scoring.write("   Game Over \n Your Score is {}".format(score),align="center", font=("Courier", 30,"bold"))
            break

    time.sleep(delay)

screen.exitonclick()