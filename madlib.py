'''
Author: Aaron Mc Nany
Date: 4/5/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
A Mad Lib is a story template that has many missing words, each indicated 
by a label giving the category (part of speech) of the missing word.  
For example, a story template will contain the word NOUNin many places instead 
of specific nouns, the word ADJECTIVEin many places instead of specific 
adjectives, etc.  Before reading the story, the reader asks listeners to provide 
the missing words without indicating where and how the words will be used in 
the story.

We will be creating a series of functions that will accept a file (the mad lib
template) and replace all of the word type indentifiers with inputs from
the user.
'''


def print_report(fname):
    '''
    This function requires one argument -- a string that represent the name
    of a file that will be used throughout the function in order to write
    a report. This report shows us the number of each of the following
    types: vowels, consonants, whitespace, and punctionuation. Not only
    does the function report the raw total of each of these, but then
    computes what percentage of the total characters each of these types
    make up of the entire file.
    '''

    file_in = open(fname, "r")

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    vtotal = 0
    ctotal = 0
    wstotal = 0
    ptotal = 0

    for line in file_in:
        for char in line.lower():
            if char in vowels:
                vtotal += 1
            elif char in consonants:
                ctotal += 1
            elif char.isspace() or char == "\n" or char == "\t":
                wstotal += 1
            else:
                ptotal += 1

    total_characters = vtotal + ctotal + wstotal + ptotal

    file_in.close()

    vpercent = round(100 * (vtotal/total_characters), 1) 
    cpercent = round(100 * (ctotal/total_characters), 1)
    wspercent = round(100 * (wstotal/total_characters), 1)
    ppercent = round(100 * (ptotal/total_characters), 1)

    print()
    print(fname.center(25, "-"))
    print(("Vowels:").ljust(20) + str(vtotal).rjust(5))
    print(("Consonants:").ljust(20) + str(ctotal).rjust(5))
    print(("Whitespace:").ljust(20) + str(wstotal).rjust(5))
    print(("Punctuation:").ljust(20) + str(ptotal).rjust(5))
    print("-" * 25)
    print(("Total:").ljust(20) + str(total_characters).rjust(5) + "\n")
    print(("Percent vowels:").ljust(20) + str(vpercent).rjust(5))
    print(("Percent consonants:").ljust(20) + str(cpercent).rjust(5))
    print(("Percent spaces:").ljust(20) + str(wspercent).rjust(5))
    print(("Percent punctuation:").ljust(20) + str(ppercent).rjust(5))
    print("=" * 25)
    print()
    
def replace_parts_of_speech(fline, type):
    '''
    This function takes two arguements, both of which are strings. The first represents
    a file line, that will be generated by a file called in a the complete_mad_lib function. 
    The second is a type of speech such as noun, verb, past verb, etc. The purpose of this 
    function is to locate all of the different types of speech in a line, then it will
    prompt the user to give an input that is relevant to that type of speech. These
    inputs are stored in a list, so that they can be written into a new copy of a file
    via complete_mad_lib.
    '''
    
    type_total = 0
    index = 0
    type_index = []
    
    while index < len(fline):
        index = fline.find(type, index)
        if index == -1: break
        type_index.append(index)
        type_total += 1
        index += len(type)
    
    if type_total == 0:
        return fline
    
    else: 
        inputs = []
        
        for i in range(type_total):
            new_input = input("Enter " + type.lower() + ": ")
            inputs.append(new_input)

            string = fline.replace(type, "{0}", 1)
            fline = string.format(inputs[i])

        return fline
  
def complete_mad_lib(ftemplate):
    '''
    This function requires one argument that comes in the form of a
    string that represents the name of a file. The goal is to write
    a new file that will replace all the occurences of a "type
    identifier" (NOUN, VERB, etc.) in the original text and replace
    it with an actual word that fits that description. This is done
    by reading the file line by line and calling replace_parts_of_speech
    in order to identify the word types and prompt the user for a response.
    '''
    
    new_file = "MAD_" + ftemplate

    fp_in = open(ftemplate, "r")
    fp_out = open(new_file, "w")

    type = ["PLURAL NOUN", "VERB PAST", "VERB", "NOUN", "ADJECTIVE"]
    
    for line in fp_in:
        for i in range(len(type)):
            string = replace_parts_of_speech(line, type[i])
            line = string
        fp_out.write(line)
           
    fp_in.close()
    fp_out.close()
#==========================================================
def main():
    '''
    Functions are called here in order to test whether or
    not the function is indeed doing what we wish for it to
    do.
    
    We also create an input object that will allow the user
    to direct the functions to the file that is desired in 
    order to complete the mad libs game.
    '''
    
    file_input = input("Enter file name: ")
    
    print_report(file_input)
    
    complete_mad_lib(file_input)


if __name__ == "__main__":
    main()
