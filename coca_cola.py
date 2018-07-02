'''
Author: Rich Thompson
Date: today
Class: ISTA 130
Section Leader: I'm the man

Description:
The program draws the name "COCA-COLA". 
'''

# all import statements here, for example:
import turtle  # this is only needed if you're using turtle graphics

# all function definitions here, we'll define functions soon


#==========================================================
def main():
    '''
    Construct a turtle and use it write 'COCO-COLA'.
    '''
    # your code goes here, make sure it's indented one level
    
    # prepare the turtle - set its state and initial position
    azt = turtle.Turtle()
    turtle.bgcolor('black') # a function in the turtle module
    azt.pencolor('red')
    azt.pensize(10)
    azt.shape('turtle')
    azt.penup()
    azt.backward(200)
    azt.pendown()
    
    # draw a C
    azt.forward(25)
    azt.backward(25)
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.penup()
    azt.right(90)
    azt.forward(25)
    azt.left(90)
    
    azt.forward(20)
    azt.pendown()
    azt.pencolor('green')
    
    # draw an O
    azt.forward(25)
    azt.backward(25)
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.left(90)
    
    azt.penup()
    azt.forward(20)
    azt.pendown()
    azt.pencolor('blue')
  
    # draw a C
    azt.forward(25)
    azt.backward(25)
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.penup()
    azt.right(90)
    azt.forward(25)
    azt.left(90)
    
    azt.forward(20)
    azt.pendown()
    azt.pencolor('gold')
    
    # draw an A
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.backward(12.5)
    azt.right(90)
    azt.forward(25)
    azt.backward(25)
    azt.right(180)
    
    azt.pencolor('magenta')
    
    # draw a hyphen
    azt.penup()
    azt.forward(20)
    azt.pendown()
    azt.forward(25)
    azt.right(90)
    azt.penup()
    azt.forward(12.5)
    azt.left(90)
    
    azt.forward(20)
    azt.pendown()
    azt.pencolor('purple')

    # draw a C
    azt.forward(25)
    azt.backward(25)
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.penup()
    azt.right(90)
    azt.forward(25)
    azt.left(90)
    
    azt.forward(20)
    azt.pendown()
    azt.pencolor('darkgoldenrod')
    
    # draw an O
    azt.forward(25)
    azt.backward(25)
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.left(90)
    
    azt.penup()
    azt.forward(20)
    azt.pendown()
    azt.pencolor('darkred')
    
    # draw an L
    azt.left(90)
    azt.forward(25)
    azt.backward(25)
    azt.right(90)
    azt.forward(25)
   
    azt.penup()
    azt.forward(20)
    azt.pendown()
    azt.pencolor('darkgreen')
    
    # draw an A
    azt.left(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.right(90)
    azt.forward(25)
    azt.backward(12.5)
    azt.right(90)
    azt.forward(25)
    azt.backward(25)
    azt.right(180)
    
    azt.hideturtle()
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
