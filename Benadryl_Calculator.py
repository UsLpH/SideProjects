from colorama import Fore, Back, Style, init
from os import system
from time import sleep

init(autoreset=True) #Set text color to normal after every output

while True:
    system("cls") # clear screen
    print(Fore.CYAN + "How Fucked Up Do You Want To Be?\n" + Fore.GREEN + "[1] Fucked Up \n" + Fore.YELLOW + "[2] Hallucinate\n" + Fore.BLUE + "[3] Trippin Balls\n" + Fore.RED + "[4] Max Level\n\n" + Fore.CYAN + "Effects:\n" +Fore.LIGHTRED_EX + "[5] Physical Effect List\n" + Fore.MAGENTA+ "[6] Hallucination Content\n") #show user options
    choice = input() #capture user input
    system("cls") #clear the screen
    if (choice not in ["1", "2", "3", "4", "5", "6"]): #check if choice is valid
        print(Fore.CYAN + "Not an option (1, 2, 3 or 4)")
        sleep(1.5)
    else:                               #if choice is valid
        if choice == "1":
            try:
                choice2 = input(Fore.CYAN + "Enter BodyWeight : ") #get bodyweight
                calc = round((1.77 * int(choice2) + 49.4)/ 25) # do math for level 2 dosage
            except ValueError:                               # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print(Fore.GREEN + f"Dosage to get fucked up : {calc} pills or {calc*25}mg") # tell user dosage
                print(Fore.YELLOW + "\nMinor Visual Hallucinations\nAuditory Hallucinations\nShort Term Memory Loss\nClosed Eye Visuals/Hallucinations (Very Random/Weird)\nLeg Restlessness\n\n")
                system("pause")
        elif choice == "2": #Hallucinations
            try:
                choice2 = input(Fore.CYAN + "Enter BodyWeight : ") #get bodyweight
                calc = round((2.52 * int(choice2) + 138)/ 25) # do math for halucinations
            except ValueError:                              # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print(Fore.YELLOW + f"Dosage to hallucinate : {calc} pills or {calc*25}mg") # tell user dosage
                print(Fore.YELLOW + "\nMajor Visual Hallucinations\nLong-Lasting Spiders\nMajor Auditory Hallucinations\nWorsened Short Term Memory Loss\nClosed Eye Visuals \n\n")
                system("pause")
        elif choice == "3": #Trippin Balls
            try:
                choice2 = input(Fore.CYAN + "Enter BodyWeight : ") #get bodyweight
                calc = round((2.92 * int(choice2) + 147)/ 25) # do math for delerium
            except ValueError:                              # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:   
                print(Fore.BLUE + f"Dosage to Trip Balls : {calc} pills or {calc*25}mg") # tell user dosage
                print(Fore.YELLOW + "\nMajor Visual Hallucinations\nMajor Auditory Hallucinations\nForget You Took Anything (May snap out of it at times)\nRestlessness\nSlurred Speech/Thoughts\n\n")
                system("pause")
        elif choice == "4": #MAX LEVEL
            try:
                choice2 = input(Fore.CYAN + "Enter BodyWeight : ") #get bodyweight
                calc = round((2.5 * int(choice2) +379)/ 25) # do math for level 3
            except ValueError:                            # check if value is valid
                print(Fore.CYAN + "Not a number")           # tell user input invalid
                sleep(2)
            else:
                print( Fore.RED + f"Delerium : {calc} pills or {calc*25}mg") # tell user dosage
                print (Fore.YELLOW + "\nMajor Visual Hallucinations\nMajor Auditory Hallucinations\nForget You Took Anything\nThink Hallucinations Are Real\nSpiders / Snakes Everywhere\nThing Dissapearing\nHallucinate Hanging Out With Friends\nHallucinate Smoking a Cigarette\n\n")
                system("pause")
        elif choice == "5": #Physical Effects
            print(Fore.YELLOW + "92.8% :" + Fore.GREEN + " Dry Mouth")
            print(Fore.YELLOW + "65.8% :" + Fore.GREEN + " Restless Legs")
            print(Fore.YELLOW + "65.8% :" + Fore.GREEN + " Accelerated Heart Rate")
            print(Fore.YELLOW + "57.7% :" + Fore.GREEN + " Dizziness")
            print(Fore.YELLOW + "51.4% :" + Fore.GREEN + " Difficulty Peeing")
            print(Fore.YELLOW + "50.5% :" + Fore.GREEN + " Muscle Spasms")
            print(Fore.RED + "38.7% :" + Fore.RED + " Cant Get Erect Temperarily")
            print(Fore.YELLOW + "35.1% :" + Fore.GREEN + " Itchiness")
            print(Fore.YELLOW + "34.2% :" + Fore.GREEN + " Nausea")
            print(Fore.RED + "27%   :" + Fore.RED + " High Blood Pressure")
            print(Fore.RED + "22.5% :" + Fore.RED + " Muscle Cramps")
            print(Fore.RED + "12.6% :" + Fore.RED + " Seizures (14 People)")
            print(Fore.RED + "1.8%  :" + Fore.RED + " Heart Attack (2 People)")
            print(Fore.RED + "0.9%  :" + Fore.RED + " Stroke (1 Person)\n\n")
            system("pause")
        elif choice == "6": #Hallucination Content
            print(Fore.YELLOW + "83.8% : " + Fore.GREEN + "Visual Drifting")
            print(Fore.YELLOW + "75.7% : " + Fore.GREEN + "Spiders or Insects")
            print(Fore.YELLOW + "68.5% : " + Fore.GREEN + "Familiar and Unfamiliar Voices")
            print(Fore.YELLOW + "62.2% : " + Fore.GREEN + "Footsteps/Doors Creaking")
            print(Fore.YELLOW + "55%   : " + Fore.GREEN + "Music")
            print(Fore.RED + "51.4% : " + Fore.RED + "Shadow people")
            print(Fore.YELLOW + "46.8% : " + Fore.GREEN + "Living Friends")
            print(Fore.YELLOW + "44.1% : " + Fore.GREEN + "An Object Turning Into Another Object")
            print(Fore.YELLOW + "42.3% : " + Fore.GREEN + "Living Family Members")
            print(Fore.YELLOW + "35.1% : " + Fore.GREEN + "Animals Besides Insects or Snakes")
            print(Fore.YELLOW + "29.7% : " + Fore.GREEN + "An Object Turning Into a Person or Animal")
            print(Fore.YELLOW + "28.8% : " + Fore.GREEN + "Strangers")
            print(Fore.YELLOW + "24.3% : " + Fore.GREEN + "Ghosts/Spirits")
            print(Fore.RED + "20.7% : " + Fore.RED + "The Hatman")
            print(Fore.RED + "15.3% : " + Fore.RED + "Demons")
            print(Fore.RED + "13.5% : " + Fore.RED + "Threatening Strangers (Police, Robbers, etc)")
            print(Fore.RED + "5.4%  : " + Fore.RED + "Dead Friends Or Acquaintances")
            print(Fore.RED + "4.5%  : " + Fore.RED + "Dead Family Members")
            print(Fore.YELLOW + "3.6%  : " + Fore.GREEN + "Angels")
            system("pause")