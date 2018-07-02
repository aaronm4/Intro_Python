'''
Author: Aaron Mc Nany
Date: 4/26/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Writing a combat script for a Role Playing Game (RPG). The combat
will take place between two fighters (class).
'''

## LIBRARIES
import random

## CLASSES
class Fighter:
    '''
    Creating a class that we will use as a means of creating
    "fighter" characters for our rpg. Each fighter will be 
    given a name, hitpoints (10), and the ability to attack
    and take damage.
    '''
    
    def __init__(self, name):
        '''
        The initializing function for our class. This function
        requires two parameters. The second is simply a string
        that will represent the name of the fighter. "self" is 
        used to attach to attributes to the fighter. For instance
        we use it to assign a name (self.name) and hitpoints
        (self.hit_points).
        '''
        
        self.name = name
        self.hit_points = 10
        
    def __repr__(self):
        '''
        This function requires only the self parameter. It is
        responsible for providing a report of the fighter's 
        current hitpoints.
        '''
        
        return(self.name + " (HP: " + str(self.hit_points) + ")")
    
    def take_damage(self, damage_amount):
        '''
        This function is used to assess damager to the fighter
        and apply it to his hitpoints. The two parameters are
        the self parameter as well as an integer that represents
        the amount of damage that needs to be attributed to the
        fighter. The function deals the damage to the fighter's
        hitpoints and then reports if they died or their current
        hitpoints.
        '''
        
        self.hit_points = self.hit_points - int(damage_amount)
        
        if self.hit_points <= 0:
            print("\tAlas,", str(self.name), "has fallen!")
        else:
            print("\t" + str(self.name) + " has " + str(self.hit_points) + " hit points remaining.")
        return None
        

    def attack(self, other):
        '''
        This function provides the fighter with the ability to 
        inflict damage on anther fighter (other represents the
        other fighter class). The function states who is attacking
        who and, if a random integer greater than or equal to 12 
        is produced by the role, then the fighter inflicts 1-6
        damage to the other fighter; otherwise, they miss.
        '''
        
        print(self.name + " attacks " + other.name + "!")
        
        success = int(random.randrange(1,21))
        
        if success >= 12:
            dmg = random.randrange(1,7)
            print("\tHits for " + str(dmg) + " hit points!")
            other.take_damage(dmg)
        else:
            print("\tMisses!")
        return None
        
    def is_alive(self):
        '''
        This function only requires the self parameter. is_alive
        simply checks if the figther's hitpoints are greater than
        0. If so, the function returns true.
        '''
        
        if self.hit_points > 0:
            return True
        else:
            return False

## FUNCTIONS            
def combat_round(fighter1, fighter2):
    '''
    This function requires two parameters, both of which
    represent an individual named fighter class. The purpose
    of combat_round is to determine who attacks who first and
    then allows the other fighter to retaliate, given they're
    still alive.
    '''
    
    turn_f1 = random.randrange(1, 7)
    turn_f2 = random.randrange(1, 7)
    
    if turn_f1 == turn_f2:
        print("Simultaneous!")
        fighter1.attack(fighter2)
        fighter2.attack(fighter1)
    
    elif turn_f1 > turn_f2:
        fighter1.attack(fighter2)
        
        if (fighter2.is_alive() == True):
            fighter2.attack(fighter1)
    
    else:
        fighter2.attack(fighter1)
        
        if (fighter1.is_alive() == True):
            fighter1.attack(fighter2)
    
    return None
            
        
        
        
        
        

#==========================================================
def main():
    '''
    We implement the game that we designed earlier and create
    two figthers, Death_Mongrel and Hurt_then_Pain. These figthers
    are locked in combat until one dies. The function gives a report
    of each turn as well. 
    '''

    Death_Mongrel = Fighter("Death_Mongrel")
    Hurt_then_Pain = Fighter("Hurt_then_Pain")
    
    rndnumber = 1
    
    while Death_Mongrel.hit_points > 0 and Hurt_then_Pain.hit_points > 0:
        
        print("\n" + ("=" * 19).ljust(19)+ " " + "ROUND " + str(rndnumber) + (" " + "="*19).rjust(19))
        print(Death_Mongrel)
        print(Hurt_then_Pain)
        
        input("Enter to Fight!")
        
        combat_round(Death_Mongrel, Hurt_then_Pain)
        
        rndnumber += 1
        
        
        
    print("\nThe battle is over!")
    print(Death_Mongrel)
    print(Hurt_then_Pain)


if __name__ == '__main__':
    main()
