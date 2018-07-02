'''
Author: Aaron Mc Nany
Date: 4/19/2018
Class: ISTA 130
Section Leader: Sam Hoeger

Description:
Creating a dictionary from a file and then using that dictionary
to print out a report of the file.
'''


def fish_dict_from_file(filename):
    '''
    This function requires one parameter which is a string that
    represents the name of a file. We create a dictionary in order
    to create our new dictionary (fishmap). We add the weight of 
    every recorded fish to its respective owner (by fish name).
    '''
    
    f_in = open(filename)
    fish_type = {'1': 'Bream', '2': 'Whitefish', '3': 'Roach','4': '?', '5': 'Smelt', '6': 'Pike', '7': 'Perch'}
    fishmap = {}
    
    for line in f_in:
        line = line.strip().split()
        line[1] = fish_type[line[1]]
        
        if line[1] not in fishmap:
            fishmap[line[1]]=[]
            fishmap[line[1]].append(float((line[2])))
        
        else:
            if (line[2]!="NA"):
                fishmap[line[1]].append(float((line[2])))
    
    f_in.close()
    return(fishmap)

#============================================================================    
def main():
    '''
    We created a dictionary called fishmap which we will essentially
    use as a new dataset in order to create a report of the count,
    mean weight, and id of each fish.
    '''
    call_fish = fish_dict_from_file("fishcatch.dat")
    
    pound = "#"
    fish_name = "NAME"
    mean = "MEAN WT"
    
    fullWeight=0.0
    print(pound.rjust(4), fish_name.ljust(10), mean.rjust(10))
    for key in sorted(call_fish):
        fish_name = key
        pound = str(len(call_fish[key]))
        sum_weight = sum(call_fish[key])
        fish_count = len(call_fish[key])
        mean = round((sum_weight/fish_count),1)
        weight = str(mean)+"g"
        print(pound.rjust(4), fish_name.ljust(10), weight.rjust(10))


if __name__ == '__main__':
    main()
