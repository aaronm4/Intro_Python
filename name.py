'''
Author: Aaron Mc Nany
Date: 2/8/18
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Using the turtle function to draw our first name (in this case: Aaron)
'''


import turtle

def draw_A(param_turtle):
    
    '''
    Draws a capital "A" letter from the starting position (lower left corner)
    and ends facing east.
    '''
    param_turtle.left(90)
    param_turtle.forward(250)
    param_turtle.right(90)
    param_turtle.forward(90)
    param_turtle.right(90)
    param_turtle.forward(250)
    param_turtle.backward(175)
    param_turtle.right(90)
    param_turtle.forward(90)
    param_turtle.backward(90)
    param_turtle.right(180)
    return None

def draw_a(param_turtle):

    '''
    Draws a lower case "A" letter from the starting position (lower left corner,
    20 units to the right of the first "A") and finishes facing east.
    '''

    param_turtle.left(90)
    param_turtle.forward(150)
    param_turtle.right(90)
    param_turtle.forward(50)
    param_turtle.right(90)
    param_turtle.forward(150)
    param_turtle.backward(75)
    param_turtle.right(90)
    param_turtle.forward(50)
    param_turtle.backward(50)
    param_turtle.right(180)
    return None
   
def draw_r(param_turtle):

    '''
    Draws a lower case "r" letter from the starting position (lower left corner,
    20 units to the right of the second "A") and finishes facing east.
    '''
    
    param_turtle.left(90)
    param_turtle.forward(150)
    param_turtle.right(90)
    param_turtle.forward(50)
    return None
  
def draw_o(param_turtle):

    '''
    Draws a lower case "o" letter from the starting position (lower left corner,
    20 units to the right of the "r") and finishes facing east.
    '''
    
    param_turtle.left(90)
    param_turtle.forward(150)
    param_turtle.right(90)
    param_turtle.forward(50)
    param_turtle.right(90)
    param_turtle.forward(150)
    param_turtle.right(90)
    param_turtle.forward(50)
    param_turtle.backward(50)
    param_turtle.right(180)
    return None
    
def draw_n(param_turtle):

    '''
    Draws a lower case "n" letter from the starting position (lower left corner,
    20 units to the right of the "o") and finishes facing east.
    '''
    
    param_turtle.left(90)
    param_turtle.forward(150)
    param_turtle.right(90)
    param_turtle.forward(50)
    param_turtle.right(90)
    param_turtle.forward(150)
    param_turtle.left(90)
    return None
    
#==========================================================
def main():
    '''
    Drawing "Aaron"
    '''
    
    ## Setting up the turtle to draw
    name_turtle = turtle.Turtle()
    name_turtle.pensize(10)
    name_turtle.speed(0)
    name_turtle.shape("turtle")
    name_turtle.penup()
    name_turtle.backward(200)
    name_turtle.pendown()
    turtle.bgcolor("white")
    turtle.pencolor("black")

    ## Drawing an A
    draw_A(name_turtle)
    
    ## Space
    name_turtle.penup()
    name_turtle.forward(20)
    name_turtle.right(90)
    name_turtle.forward(175)
    name_turtle.left(90)
    name_turtle.pendown()
    
    ## Drawing an smaller A
    draw_a(name_turtle)
    
    ## Space
    name_turtle.penup()
    name_turtle.forward(20)
    name_turtle.right(90)
    name_turtle.forward(75)
    name_turtle.left(90)
    name_turtle.pendown()
    
    ## Drawing an r
    draw_r(name_turtle)
    
    ## Space
    name_turtle.penup()
    name_turtle.forward(20)
    name_turtle.right(90)
    name_turtle.forward(150)
    name_turtle.left(90)
    name_turtle.pendown()
    
    ## Drawing an o
    draw_o(name_turtle)
    
    ## Space
    name_turtle.penup()
    name_turtle.forward(20)
    name_turtle.pendown()
    
    ## Drawing an n
    draw_n(name_turtle)
    
    ## Putting turtle in position to draw a new letter
    name_turtle.penup()
    name_turtle.forward(20)
    name_turtle.pendown()
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
