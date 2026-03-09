#variables
sansui_condition = 100
decrease_value = 5
yes_no = ["yes", "no"]
actions = ["lift", "screw", "unscrew", "solder", "unsolder", "wipe down", "inspect", "multimeter"]
#husk på at når man tilføjer noget i list, at man også skal skrive dem ind i if, elif og else statements senere.
#som der blev gjort her, så har jeg bare sagt, skip til næste næste sektion for at gøre det nemmer, men man kunne godt trække liv fra!

# funktioner
def damage():
    global sansui_condition  #s. 247-248
    #Gad, vide om det her er grunden til at det ikke virker længder nede? (global)

    sansui_condition -= decrease_value
    return sansui_condition

def player():
    print(input('Welcommen to the hifi game press enter to start the repair-game'))

    name = input("Enter your name: ")
    print(input("Imagine...." + name + "... you bought a pinnacle of hifi and now its time to enjoy it..."))

def intro ():

    print(input('You sit in your living room, sipping a nice cup of coffee'))

    print(input('Your Sansui au-555a is playing and life is perfect...'))

    print(input('...until'))

    print(f'A funky smell billows up from, your beloved Sansui au 555a.  Loss of value of the Sansui au 555a is {damage()}% ')

    #while loop!
    response = ""
    while response not in yes_no:
        response = input("Can you fix it? (Enter yes or no)\t")

        if response == "yes":
            print(input("You race to the Sansui au 555a and frantically starts unpluggning all the cables "))
            print(f'Loss of value of the Sansui au 555a is  {damage()} ')
            start_game()

        elif response == "no":
            print(input("You sit paralyzed."))
            print(input("kaaabooooom. The Sansui au 555a blows up. GAME OVER. "))
            quit()

        else:
            print("I didn't understand that. ")

def start_game():
    response = ""
    while response not in actions:
        print(input("You stand in front of the Sansui au 555a. "))
        print(input("You pause for a second and bring it to your office... "))

        response = input("what actions do you take lift/screw/unscrew/solder/unsolder/wipe down/inspect/multimeter ")

        if response == "lift":
            print(input("You try to rip of the lit witout luck. "))
            print(f'Loss of value of the Sansui au 555a is  {damage()} ')
            continue_game_hard()

        elif response == "screw":
            print(input("You tighten the screws "))
            print(f'Loss of value of the Sansui au 555a is  {damage()} ')
            continue_game_hard()

        elif response == "unscrew ":
            print(input("You succesfully unscrew the lit of the Sansui au 555a. "))
            continue_game()

        elif response == "solder ":
            print(input('in your panic you greb the soldering iron instead of the screwdriver. '))
            print(input("GAME OVER. "))
            quit()

        elif response == "unsolder ":
            print(input("You greb the soldering iron and pause, and release how dumb it is. "))
            print(input("GAME OVER. "))
            quit()

        elif response == "wipe down ":
            print(input("You clean the outsite of the Sansui au 555a. "))
            print(f'Increase value of the Sansui au 555a is  {damage()+5}')
            continue_game_hard()

        elif response == "inspect ":
            print(input("You inspect the outsides of the Sansui au 555a."))
            print(input("... but that doesnt open the lit..."))
            print(f'Loss of value of the Sansui au 555a is  {damage()} ')
            continue_game_hard()

        elif response == "multimeter":
            print(input("You try to use the multimeter as a screwdriver... and fail and brake it...."))
            print(f'Loss of value of the Sansui au 555a is  {damage()} ')
            continue_game_hard()

        else:
            print("I didn't understand that.\n ")

def continue_game_hard():
    response = ""
    while response not in actions:
        print(input("You have fail miserably... "))
        print("... the smell is getting worse ")

        response = input("You know what you have to do... think very hard..... (hint: un...) ")

        if response == "unscrew":
            print(input("you sit the Sansui au 555a back down. "))
            print(input("You breath in and out. With clear thought you grab the screwdriver. "))
            print(input("after 2 hours you finally get the lit of "))
            print(f'Loss of value of the Sansui au 555a is {damage()-55} ')
            continue_game()

        else:
            print("I didn't understand that.\n ")

def continue_game():
    response = "" #lokal variable!
    while response not in actions:
        print(input("You have finally gotten the lit of the Sansui au 555a"))

        response = input("what actions do you take lift/screw/unscrew/solder/unsolder/wipe down/inspect/multimeter ")

        if response == "inspect":
            print(input("You inspect the insides of the Sansui au 555a, look for what coursed the damage"))

#hovedfunktionen:
def main():
    main_game = 'y'
    while main_game == 'y':
        player()
        intro()
        main_game = input('(press y to continue or n to stop):\t')

#kalder hele spillet!
main()
