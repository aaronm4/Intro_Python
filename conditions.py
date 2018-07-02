'''
Author: Aaron Mc Nany
Date: 2/22/18
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Exploring the use of conditionals in functions. Specifically learning how to
expand on what we have learned about the "if" function.
'''

def word_length(string, num):
    '''
    A function that requires two parameter. String is, well, a string; to be specific
    to this assignment, it is a word. The function will see if the length of that word
    is longer than the specified integer parameter, num, and then print the respective
    statement.
    '''
    
    if len(string) > num:
        print("Longer than", num, "characters:", string)
    elif len(string) < num:
        print("Shorter than", num, "characters:", string)
    else:
        print("Exactly", num, "characters:", string)

def stop_light(light, time):
    '''
    A function that requires two arguments. Light is the color of the light at the given
    stop light that we want to specify. The time parameter dictates how long this light 
    has been showing. We are given specifications such that if we can describe if the 
    color has changed or not. 
    '''
    
    if light == 'green' and time > 60:
        return 'yellow'
    elif light == 'yellow' and time > 5:
        return 'red'
    elif light == 'red' and time > 55:
        return 'green'
    else:
        return light

def is_normal_blood_pressure(sys,dia):
    '''
    The sys paramter is a patient's systolic and dia is diastolic. These measurements
    can be used to determine if a person's blood pressure is in the normal range. 
    If sys and dia are both below 120 and 80 respectively, this person is considered
    to be within the normal range.
    '''
    
    if sys < 120 and dia < 80:
        return True
    return False

def doctor():
    '''
    The doctor function requires no parameters, but rather uses inputs. It does
    essentially the same as the above function, which can be noted since we
    call said function, except requires the user to input the values rather
    than predefining them in a function call in main.
    '''
    
    sys = int(input("Enter your systolic reading: "))
    dia = int(input("Enter your diastolic reading: "))
    
    if(is_normal_blood_pressure(sys,dia)):
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")

def pants_size(num):
    '''
    Requires only one parameter, which is an integer. Pant sizes can be described
    qualitatively (large, medium, small) or via numerical measurement of the waist.
    The parameter in pants_size is the numerical measurement, and the function will
    translate that into the qualitative descriptor. 
    '''
    
    if num >= 34:
        return "large"
    if num >= 30:
        return "medium"
    return "small"


def pants_fitter():
    '''
    Another function that does not require parameters, but rather utilizes
    the previous function. The function asks the user to input their name, waist,
    how many pairs of pants they require, and the style. The end result is that it
    prints how the earlier specified information as well as a price that is a
    function of the style (fancy or regular) and the number of pants.
    '''
    
    name = input("Enter your name: ")
    
    print("Greetings", name, "welcome to Pants-R-Us")
    
    waist = int(input("Enter your waist size in inches: "))
    num_pants = int(input("How many pairs of pants would you like: "))
    style = input("Would you like regular or fancy pants? ")
    
    if style == "fancy":
        total = 100 * num_pants
    else:
        total = 40 * num_pants
    print(num_pants, "pairs of", pants_size(waist),style,"pants: $",total)



def digdug(num):
    '''
    Checks an integer, num, to see if it is divisible by 3 and 5. If it is divisible
    by both, then it prints the number and the respective string (digdug in this case).
    If it is not divisible by both, then it checks each number and prints their
    respective strings. If it is not divisible by 3 or 5, then it returns nothing.
    '''
    
    for i in range(1, num+1):
        if i%3 == 0 and i%5 == 0:
            print(i, ": digdug")
        elif i%3 == 0:
            print(i, ": dig")
        elif i%5 == 0:
            print(i, ": dug")
        else:
            continue
       
def beef_type(percent_lean):
    '''
    Checks the given percentage of how lean our beef is in the parameter, and
    then proceeds to categorize our meat by checking whether it meets (no pun
    intended) our specified qualifications below. If percent_lean is greater
    than 95, then it returns "Unknown."
    '''
    
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean < 85:
        return "Chuck"
    elif percent_lean < 90:
        return "Round"
    elif percent_lean <= 95:
        return "Sirloin"
    else:
        return "Unknown"

def species_height(species, height):
    '''
    The first parameter is basically used to determine if we are talking about
    humans or any other species, and then uses that to run the height parameter
    against two different sets of criteria.
    '''
    
    if species == 'Human':
        if height < 67:
            print("Below Average")
        elif height > 67:
            print("Above Average")
        else:
            print("Average")
    else:
        if height < 71:
            print("Below Average")
        elif height > 71:
            print("Above Average")
        else:
            print("Average")

def sooner_date(month1, day1, month2, day2):
    '''
    Use to tell determine which date is earlier (using integer parameters). Since 
    months supersede days, then we determine the earlier data first by the month. 
    Which month entered has a lower value, i.e. comes first in the calender year,
    will be printed with its respective day. If the months are equivalent, then
    the second if function determines which day comes first.
    '''
    if month1 < month2:
        print(month1, "/", day1)
    elif month2 < month1:
        print(month2, "/", day2)
    else:
        if day1 < day2:
            print(month1,"/",day1)
        else:
            print(month2, "/",day2)


#==========================================================
def main():
    '''
    Test the above functions to ensure that they work correctly.
    '''
    
    digdug(6)



if __name__ == '__main__':
    main()
