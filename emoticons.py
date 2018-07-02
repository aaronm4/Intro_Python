'''
Author: Aaron Mc Nany
Date: 4/19/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Appending existing dictionaries with new information from a file
and creating a report based on the most common emoticon.
'''



    
    
def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    '''
    This function takes three parameters, which are all strings.
    The first represents the name of a file from which we will be
    gathering information to append the following two parameters, 
    which are existing dictionaries that are fed to us. All the
    function does is add any values from the file, that are not
    in their current respective dictionaries, to said respective
    dictionaries.
    '''
    
    f_in = open(filename)
    
    for line in f_in:
        line = line.replace("\"", "")
        line = line.strip().split()
        
        if line[0] not in emoticons_to_ids:
            emoticons_to_ids[line[0]]=[]
        emoticons_to_ids[line[0]].append((line[2]))
    
        if (line[2] not in ids_to_emoticons):
            ids_to_emoticons[line[2]]=[]
        ids_to_emoticons[line[2]].append((line[0]))
        
    f_in.close()

def find_most_common(dict):
    '''
    This function requires one parameter that is the dictionary
    through which we will search in order to find the most
    frequently used emoticon in said dictionary. The function
    will print out the emoticon with the number of times it
    occurs as well as return the name of the key.
    '''
    
    length=0
    key_name=""
    
    for key in dict:
        
        if (length<len(dict[key])):
            length = len(dict[key])
            key_name = key
    
    print (key_name.ljust(20), "occurs" , str(length).rjust(8), "times")
    return key_name
    
    

#============================================================================    
   
def main():
    '''
    We create two empty dictionaries that we will append using
    our load_twitter_dicts_from_file function. We then print
    out a report stating how many times each emoticon occurred.
    '''
    
    emoticons_to_ids = {}
    ids_to_emoticons = {}
    load_twitter_dicts_from_file("twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons)
    
    print("Emoticons:", len(emoticons_to_ids))
    print("UserIDs:  ", len(ids_to_emoticons))
    
    for i in range (5):
        emoticons_to_ids.pop(find_most_common(emoticons_to_ids))
    



if __name__ == '__main__':
    main()
