# import figlet, sys, and random
from pyfiglet import Figlet
import sys
import random

# declaring a variable figlet which will equal Figlet()
figlet = Figlet()



# check if argv has no command line arguments
if len(sys.argv) == 1:
    #asking user for input to display in figlet
    inpt = input("Enter text: ")
    # if so randomly choose a font
    random.choice(figlet.getFonts())
    # and finally print the text
    print(figlet.renderText(inpt))
    # exit with code 0
    sys.exit(0)

#   check if argv has only 2 command line arguments and if the first one is -f and the second one is in the getfonts list
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet.getFonts():
    #asking user for input to display in figlet
    inpt = input("Enter text: ")
    # declare a variable f and make it equal to setfont of the user
    figlet.setFont(font=sys.argv[2])
    # finally print the text
    print(figlet.renderText(inpt))
    # exit with code 0 indicating true
    sys.exit(0)

else:
    # if both are false exit with  code 1 indicating false
    print("Invalid Usage")
    sys.exit(1)