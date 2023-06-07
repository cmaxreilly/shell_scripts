
#OBJECTIVE:
# Create a script that takes a command line input, converts that command line inpute to snake case, then makes that
# command line input the filename and title of a new file in my feynman_technique folder in my vault. The script will
# then append 3 lines of space, followed by the text "press R to insert explanation here," followed by 3 more lines of
# space. This will then do the same thing with a simplified explanation.

#Modules
import os

# Take command line input of concept to be learned

def concept_input():
	concept = str(input("What concept would you like to learn? "))
	return (concept)

# print(concept_input())


# Convert to snake case

def sneky_case(string):
    string = list(string);
    n = len(string);
    
    for i in range(n) :
        if (string[i] == " ") :
            string[i] = "_" ;

        else:
            string[i] = string[i].lower();

    string = "".join(string)
    return string

print(sneky_case("Poopy Goopy Doopy"))
# print(sneky_case(concept_input))


# Make snake case phrase into file name, as well as append date


# Append original name, date in Month/dd/yyyy format, 3 blank lines, "Complex Description", <Insert Text here with 'R'>, 3 blank lines, "Simplified Description", <Insert Text here with 'R'>



# Vim filename starting at appropriate line, most likely <Insert> under Complex Description.

