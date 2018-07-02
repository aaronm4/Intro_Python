'''
LAB 6
Name: Aaron Mc Nany
Date: 2/28/18
Class: ISTA 130

Description:
This program contains several unrelated functions that make use of if
statements and while loops.
'''

import random

def can_pay(cash, cost):
    '''
    USE YOUR CAN_PAY FUNCTION FROM LAST WEEK'S DISCUSSION
    
    Return True if there is enough money to pay for an activity. Return False and print an error message if there is not enough money.
    
    money (float) -- The amount of money you have at the start of the function
    cost (float) -- The price of an activity
    '''
    if float(cash) >= float(cost):
        return True
    if float(cash) < float(cost):
        print("Error")
        return False
        
def ride_rollercoaster(money):
    '''
    Note: use the code provided in the discussion lecture video where the section leader 
    walks you through this function. THE TEST FILE DOES NOT TEST THIS FUNCTION because it
    was provided for you.

    Allow the user to ride the rollercoaster if they have enough money.

    Checks first if the user has enough money through the can_pay function,
    and if they do, then print out a ride message and return their new total
    amount of money after the ride.
    Ask the user to ride until they say no or until they can't pay.

    Parameters:
    money - an int representing how much money the user has

    Returns:
    - The amount of money the user has after the transaction
    '''
    
    print("Space Jam: 1.00\nBig One: 1.75\nBigger One: 2.75")
    
    while True:
        choice = input("Which ride do you want to ride? ")
        
        if choice == "Space Jam":
            if can_pay(money, 1.00) == True:
                print("Enjoy the ride!")
                money = money - 1.00
            else:
                return money
                
        elif choice == "Big One":
            if can_pay(money, 1.75) == True:
                print("Enjoy the ride!")
                money = money - 1.75
            else:
                return money
        
        elif choice == "Bigger One":
            if can_pay(money, 2.75) == True:
                print("Enjoy the ride!")
                money = money - 2.75
            else:
                return money
        else:
            print("That\'s not a ride, try again!")
        
        answer = input("Do you want to ride another ride? Y/N ")
        
        if answer == "n" or answer == "N":
            break
    
    return money
    
def buy_food(money):
    '''
    Note: the food menu you should print out is provided for you. Make sure to use these specific 
    prices when you are subtracting from the user's money. When you are getting input from the user
    to ask if they would like to continue ordering, make sure their answer is in the format 'y' for yes
    and 'n' for no.

    Allows the user to buy some food if they have enough money.
    Ask the user for an order until they say no or until they can't pay.

    Parameters:
    money - an int representing how much money the user has

    Returns:
    - The amount of money the user has after the transaction
    '''

    print('hotdog: 1.00\nburger: 2.00\nsoda: 0.50')
    
    while True:
        choice = input("Which ride do you want to ride? ")
        
        if choice == "hotdog":
            if can_pay(money, 1.00) == True:
                print("Enjoy the ride!")
                money = money - 1.00
            else:
                return money
                
        elif choice == "burger":
            if can_pay(money, 2.00) == True:
                print("Enjoy the ride!")
                money = money - 2.00
            else:
                return money
        
        elif choice == "soda":
            if can_pay(money, 0.50) == True:
                print("Enjoy the ride!")
                money = money - 0.50
            else:
                return money
        else:
            print("That\'s not a ride, try again!")
        
        answer = input("Do you want to ride another ride? Y/N ")
        
        if answer == "n" or answer == "N":
            break
    
    return money
    
def guessing_game(money):
    '''
    Note: when you are asking the user if they would like to play again, make sure their answer is 
    in the format 'y' for yes and 'n' for no.

    Allows the user to play a guessing game for two dollars.
    Ask the user to play until they say no or until they can't pay.

    Parameters:
    money - an int representing how much money the user has

    Returns:
    The user's money - 2 if they failed to guess the correct number in 4 tries
    or the user's money + 20 if they correctly guess the number.
    '''
     
    while True:
        random_number = random.randint(0, 100)
        guess_count = 0
        
        while guess_count < 4:
            choice = int(input("Guess a number: "))
            
            if choice == random_number:
                print("Correct!")
                money = money + 20
            
                break
            
            if choice < random_number:
                print("Too low")
                guess_count = guess_count + 1
                
            else:
                print("Too high")
                guess_count = guess_count + 1
        
        if guess_count == 4:
            if can_pay(money, 2) == True:
                print("Too many guesses. You lose!")
                money = money - 2
            
            else:
                return money
        
        answer = input("Would you like to play again? Y/N ")
        
        if answer == "n" or answer == "N":
            break
    
    return money
    
def main():
    '''
    NOTE: MAIN IS OPTIONAL AND WILL NOT BE TESTED BY THE TEST FILE. If you would like to try to
    write main just for fun, assign the total_money variable to 100 so the user starts with $100. Make 
    the user's options 'ride a ride', 'get food', 'play a game', and 'end'.

    If you want to test your main, open the amusement_park_test.py file and uncomment the test_main
    function at the bottom.

    Test the above functions to ensure that they work correctly.
    '''
    

if __name__ == '__main__':
    main()