'''
Author: Aaron Mc Nany
Date: 2/15/18
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Learning how to use for loops in Python and integrating said function
with other python functions such as if, print, etc.
'''


import math

def print_word(int, word):
    '''
    Function requires two inputs. The first being an integer and the second being a word.
    The function will then count up to said integer from 1 and for every row print
    "-->" and then the word in the same row.
    '''
    for y in range (0, int):
        print(y+1, "-->", word)
 
def bacteria(minutes, bacteria):
    '''
    Function requires two inputs; both of which are integers. The first parameter, defines how
    many minutes occur between each observation starting at whatever integer is entered. 
    The second parameter describes the number of observations to be taken. Since each
    bacteria has two offspring, we want the generation to multiply for each observation
    taken (this is done with the *= operator).
    '''
    generation = 2
    for x in range(bacteria):
        time_interval = (x+1)*minutes
        print("after", str(time_interval), "minutes: ", generation, "bacteria")
        generation *=2

def convert_to_copper(gold, silver, copper):
    '''
    Function requires three inputs; all of which are integers describing how many 
    of each coin are to be considered. It will print the coins to be considered in
    the first portion of the print statement, and then display the value in just 
    copper using the given conversion rates.
    '''
 
    print(gold, "gp,", silver, "sp,", copper, "cp converted to copper is:", (gold*10*5)+(silver*5)+copper, "cp")

def convert_from_copper(copper_coins):
    '''
    Function requires one input, which is an integer. The parameter, copper_coins,
    represents how many copper coins we want to exchange for as many gold pieces
    as possible, then as many silver pieces as possible, and finally print the
    remaining copper coins.
    '''
    
    copper_gold = int(copper_coins/50)
    copper_silver = int((int(copper_coins % 50))/5)
    copper_remain = (int(copper_coins % 50) % 5)
    
  
    
    print(copper_coins, "copper pieces is:", copper_gold, "gp,", copper_silver, "sp,", copper_remain, "cp")
    
def repeat_word(word, rows, columns):
    '''
    Function requires three inputs. The first is a string representing a word.
    The other two (rows and columns) are integers. The function will repeat the
    string given as the word parameter in a matrix with as many rows and columns
    specified in the other two parameters.
    '''
    for z in range(rows):
        print(word*columns)
        
def text_triangle(triangle_param): 
    '''
    Function requires one input. The input describes the number of "X" characters
    to print. Starting from one, the function will print one "X" on row one, two "X"
    characters on row two, so on and so forth. If the integer entered is less than
    or equal to zero, then only a blank line will be printed.
    '''
    X = "X"
    for a in range(triangle_param):
        if triangle_param > 0:
            print(str(X)*(a+1))
    if triangle_param <= 0: 
        print()
            
def surface_area_of_cylinder(radius, height):
    '''
    Function requires two inputs; both of which can be floats. The function 
    will state the dimensions of a cylinder with the specified radius and
    height, then compute the surface area using the formula for surface 
    area of a cylinder. 
    '''
    
    print("The surface area of a cylinder with radius", float(radius), "and height", float(height), "is", 2*(math.pi)*(radius**2) + 2*(math.pi)*radius*height)
    
def tree_height(distance, length):
    '''
    Function requires two inputs; both of which are integers. The function
    will state the specified kite string length and distance from the kite
    wielder to the three. This forms a triangle where the string length
    is the hypotenuse and the distance is the base. We can use properties
    of a triangle in order to calculate the height of the tree.
    '''
    
    print("Kite string:", length)
    print("Distance:", distance)
    print("Height:", math.sqrt((length**2)-(distance**2)))
#==========================================================
def main():
    '''
    Test the above functions to ensure that they work correctly.
    '''
    
    print_word(5, "banana")
    
    bacteria(21, 3)
    
    convert_to_copper(15, 23, 12)
    
    convert_from_copper(3242)
    
    repeat_word("Goblin", 3, 5)
    
    text_triangle(0)
    
    surface_area_of_cylinder(10.0, 10.0)
    
    tree_height(300, 500)
    

if __name__ == '__main__':
    main()
