from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
#this allows the user to input the color of their choice
color = input('Enter a color:')
#these are the colors the user can pick from
color_choice = ["red","orange","yellow","green","blue","purple"]
t.pencolor(color)

#this allows the user to pick the number of sides in the shape
your_shape = input ('How many sides will your shape have?')
int_your_shape = int(your_shape)
t.pendown()

#this should make the shape. It would repeat each action depending on how many
#sides the shape has
for shape in range (int_your_shape)
    t.forward(50)
    t.right(360/int_your_shape)

for square_shape in range(4): #repeats 4 times because a square has 4 sides
    t.pendown()
    t.forward(75)
    t.right(90)

#this is so triangle isn't connected to square
for move in range(1):
         t.penup()
         t.forward(100)

for triangle in range(3):
    t.pendown()
    t.forward(75)
    t.right(120)





# Close window on click.
exitonclick()
