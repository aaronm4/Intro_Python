'''
Author: Aaron Mc Nany
Date: 3/1/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
<summary of this program>
'''

import random

def print_scores(player1, score1, player2, score2):
    '''
    Function requires four parameters. Both player1 and player2 are strings that will be the names
    of the players given via an input function in main. The other two, score1 and score2, are integers
    that describe the scores of each player. This function is essentially a scoreboard. 
    '''
    
    print()
    
    print("--- SCORES" + "\t" + player1 + ": " + str(int(score1)) + "\t" + player2 + ":" + " " + str(int(score2)) + " ---")
    
def check_for_winner(namewin, scorewin):
    '''
    Pig ends when a player reaches a score of 50. This function requires two inputs, the first being
    a string that is the name of the player that we want to check to see if they won. The second 
    parameter is an integer that represents the current score of the player. If scorewin is 
    greater than or equal to 50, the game ends and it prints the winner statement.
    '''
    
    if scorewin >= 50:
        print("THE WINNER IS: " + namewin + "!!!!!")
        return True
    else:
        return False
        
def roll_again(name_roll):
    '''
    This function is designed to ask the designated player whether or not they wish to continue
    rolling or to stop and collect their points from that turn.
    '''
    
    while True:
        roll = input("Roll again, " + name_roll + "? (Y/N) ")
    
        if roll == "Y" or roll == "y":
            return True
        elif roll == "N" or roll == "n":
            return False
        else:
            print("I don\'t understand: \"" + roll + "\". " + "Please enter either \"Y\" or \"N\".")
 
def play_turn(current_player):
    '''
    This function is the crux of the game. It uses the previously defined functions in order
    to "roll the dice" add the points to a variable designed as the points for the turn, and
    eventually end the turn either by player choice or if the player "rolls" a 1. 
    '''
    
    print("---------- " + current_player + "\'s turn ----------")
    
    turn_score = 0
    
    while True:
        points = random.randint(1, 6)
        
        print("\t<<< " + current_player + " rolls a " + str(points) + " >>>")
        if points != 1:
            turn_score = turn_score + points
            print("\tPoints: " + str(turn_score))
        else:
            print("\t!!! PIG! No points earned, sorry " + current_player + " !!!")
            turn_score = 0
            input("(enter to continue)")
            break
            
        
        
        if roll_again(current_player) == True:
            continue
        else:
            break
            
    return turn_score
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    
    seed = input("Enter seed value: ")
    
    random.seed(int(seed))
    
    print()
    print()
    
    print("Pig Dice")
    
    p1 = input("Enter name for player 1: ")
    p2 = input("Enter name for player 2: ")
    
    print("\t" + "Hello " + p1 + " and " + p2 + ", welcome to Pig Dice!")
    
    score_p1 = 0
    score_p2 = 0
    

    print_scores(p1, score_p1, p2, score_p2)
    
    while True:
        points1 = play_turn(p1)
        
        score_p1 = score_p1 + points1
        
        print_scores(p1, score_p1, p2, score_p2)
        
        if score_p1 >= 50:
            print("THE WINNER IS: " + p1 + "!!!!!")
            break
        else: 
            points2 = play_turn(p2)
            
            score_p2 = score_p2 + points2
            
            print_scores(p1, score_p1, p2, score_p2)
            
            if score_p2 >=50:
                print("THE WINNER IS: " + p2 + "!!!!!")
                break
            else:
                continue
        
            

if __name__ == '__main__':
    main()
