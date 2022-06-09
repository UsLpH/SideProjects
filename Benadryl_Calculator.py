from colorama import Fore, Back, Style, init
from os import system
from time import sleep

init(autoreset=True) #Set text color to normal after every output

while True:
    system("cls") # clear screen
    print(Fore.CYAN + "How Fucked Up Do You Want To Be?\n" + Fore.GREEN + "[1] Fucked Up \n" + Fore.YELLOW + "[2] Halucinate\n" + Fore.BLUE + "[3] Trippin Balls\n" + Fore.RED + "[4] Max Level") #show user options
    choice = input() #capture user input
    system("cls") #clear the screen
    if (choice not in ["1", "2", "3", "4"]): #check if choice is valid
        print(Fore.CYAN + "Not an option (1, 2, 3 or 4)")
        sleep(4)
    else:                               #if choice is valid
        choice2 = input(Fore.CYAN + "Enter BodyWeight : ") #get bodyweight
        if choice == "1":
            try:
                calc = round((1.77 * int(choice2) + 49.4)/ 25) # do math for level 2 dosage
            except ValueError:                               # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print(Fore.GREEN + f"Dosage to get fucked up : {calc} pills or {calc*25}mg") # tell user dosage
                system("pause")
        elif choice == "2":
            try:
                calc = round((2.52 * int(choice2) + 138)/ 25) # do math for halucinations
            except ValueError:                              # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print(Fore.YELLOW + f"Dosage to halucinate : {calc} pills or {calc*25}mg") # tell user dosage
                system("pause")
        elif choice == "3":
            try:
                calc = round((2.92 * int(choice2) + 147)/ 25) # do math for delerium
            except ValueError:                              # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:   
                print(Fore.BLUE + f"Dosage to Trip Balls : {calc} pills or {calc*25}mg") # tell user dosage
                system("pause")
        elif choice == "4":
            try:
                calc = round((2.5 * int(choice2) +379)/ 25) # do math for level 3
            except ValueError:                            # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print( Fore.RED + f"Delerium : {calc} pills or {calc*25}mg") # tell user dosage
                system("pause")