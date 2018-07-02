'''
Author: Aaron Mc Nany
Date: 2/8/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Creating a snake like design using the turtle library
'''

import turtle

def triangle(turtle_name, length):

    '''
    Draws a triangle starting from the "base" being a straight line
    to the north. Returns to the starting position and faces east
    '''
    
    turtle_name.left(90)
    turtle_name.forward(length)
    turtle_name.left(120)
    turtle_name.forward(length)
    turtle_name.left(120)
    turtle_name.forward(length)
    turtle_name.setheading(0)
    return None

def square(turtle_name, length):

    '''
    Draws a square starting from the lower left and drawing
    the left side first. Returns to the starting position and 
    faces east.
    '''
    
    turtle_name.left(90)
    turtle_name.forward(length)
    turtle_name.right(90)
    turtle_name.forward(length)
    turtle_name.right(90)
    turtle_name.forward(length)
    turtle_name.right(90)
    turtle_name.forward(length)
    turtle_name.setheading(0)
    return None
    
def pentagon(turtle_name, length):

    '''
    Draws a pentagon starting from the lower right and drawing
    the base side first. Returns to the starting position and 
    faces east.
    '''
    
    turtle_name.left(90)
    turtle_name.forward(length)
    turtle_name.right(72)
    turtle_name.forward(length)
    turtle_name.right(72)
    turtle_name.forward(length)
    turtle_name.right(72)
    turtle_name.forward(length)
    turtle_name.right(72)
    turtle_name.forward(length)
    turtle_name.setheading(0)
    return None

def hexagon(turtle_name, length):

    '''
    Draws a hexagon starting from the lower right and drawing
    the base side first. Returns to the starting position and 
    faces east.
    '''
    
    turtle_name.left(90)
    turtle_name.forward(length)
    turtle_name.right(60)
    turtle_name.forward(length)
    turtle_name.right(60)
    turtle_name.forward(length)
    turtle_name.right(60)
    turtle_name.forward(length)
    turtle_name.right(60)
    turtle_name.forward(length)
    turtle_name.right(60)
    turtle_name.forward(length)
    turtle_name.setheading(0)
    return None    



#==========================================================
def main():
    '''
    Drawing the snake using the previously defined functions.
    '''
    
    ## Setting up the turtle to draw
    snake_turtle = turtle.Turtle()
    snake_turtle.pensize(10)
    snake_turtle.speed(0)
    snake_turtle.shape("turtle")
    snake_turtle.penup()
    snake_turtle.backward(200)
    snake_turtle.pendown()
    turtle.bgcolor("white")
    
    ## Drawing left most triangle
    snake_turtle.pencolor("green")
    triangle(snake_turtle, 100)
    
    ## Drawing left most square
    snake_turtle.pencolor("black")
    square(snake_turtle, 100)
    
    ## Drawing left most hexagon
    snake_turtle.pencolor("goldenrod")
    snake_turtle.penup()
    snake_turtle.goto(-100, 0)
    snake_turtle.pendown()
    hexagon(snake_turtle, 100)
    
    ## Drawing right most hexagon
    snake_turtle.pencolor("goldenrod")
    snake_turtle.penup()
    snake_turtle.goto(70, 0)
    snake_turtle.pendown()
    hexagon(snake_turtle, 100)
    
    ## Drawing pentagon
    snake_turtle.pencolor("black")
    snake_turtle.penup()
    snake_turtle.goto(240, 0)
    snake_turtle.pendown()
    pentagon(snake_turtle, 100)
    
    ## Drawing inner triangles
    snake_turtle.pencolor("red")
    snake_turtle.penup()
    snake_turtle.goto(72, 0)
    snake_turtle.pendown()
    triangle(snake_turtle, 100)
    
    snake_turtle.pencolor("red")
    snake_turtle.penup()
    snake_turtle.goto(240, 0)
    snake_turtle.pendown()
    triangle(snake_turtle, 100)
    
    snake_turtle.pencolor("red")
    snake_turtle.penup()
    snake_turtle.goto(-100, 100)
    snake_turtle.setheading(180)
    snake_turtle.pendown()
    triangle(snake_turtle, 100)
    
    snake_turtle.pencolor("red")
    snake_turtle.penup()
    snake_turtle.goto(72, 100)
    snake_turtle.setheading(180)
    snake_turtle.pendown()
    triangle(snake_turtle, 100)
    
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
