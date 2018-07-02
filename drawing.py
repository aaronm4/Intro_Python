'''
Author: Aaron Mc Nany
Date: 2/8/18
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Using what we learned from the first two problems in order to
make a drawing of our own.
'''

import turtle

def circle(param_turtle, radius, arc):

    '''
    Draws a circle that takes a turtle parameter, a parameter for the
    radius, and a paramter for the arc length (360 degrees being a full 
    circle.
    '''
    param_turtle.circle(radius, arc)
    param_turtle.setheading(0)
    return None
    
def octagon(param_turtle, length):

    '''
    Draws an octagon that takes both a turtle parameter as well as
    a parameter for the length of the sides.
    '''
    
    param_turtle.setheading(0)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    param_turtle.left(45)
    param_turtle.forward(length)
    return None
    

    


#==========================================================
def main():
    '''
    Draws one full cirlce, two semi-circles each with a smaller radius. Also draws
    three octagons that give the illusion of being linked together.
    '''
    
    ## Setting up the turtle to draw
    wolf = turtle.Turtle()
    wolf.speed(0)
    wolf.shape("turtle")
    wolf.pensize(10)
    turtle.bgcolor("black")
    
    ## Main circle
    wolf.pencolor("white")
    wolf.penup()
    wolf.goto(0, -315)
    wolf.pendown()
    circle(wolf, 300, 360)
    
    ## Second circle
    wolf.pencolor("red")
    wolf.penup()
    wolf.goto(0, -250)
    wolf.pendown()
    circle(wolf, 240, 290)
    
    ## Third circle
    wolf.pencolor("red")
    wolf.penup()
    wolf.goto(0, -169)
    wolf.pendown()
    circle(wolf, 167, 290)
    
    ## Octagon 1
    wolf.pencolor("white")
    wolf.penup()
    wolf.goto(-15, 0)
    wolf.pendown()
    octagon(wolf, 50)
    
    ## Octagon 2
    wolf.pencolor("orange")
    wolf.penup()
    wolf.goto(35, -50)
    wolf.pendown()
    octagon(wolf, 50)
    
    ## Octagon 3
    wolf.pencolor("blue")
    wolf.penup()
    wolf.goto(-65, -50)
    wolf.pendown()
    octagon(wolf, 50)
    
    
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
