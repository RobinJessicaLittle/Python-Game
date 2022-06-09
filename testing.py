#IMPORTS
import random
import os
import sys
from time import sleep
from turtle import clear
from operator import add, sub, mul

#SETUP VARIABLES
your_name = ""
inventory = []
animals = ['Pigeon','Fox','Rat']
animals_ind = ['(1)','(2)','(3)']

#MECHANIC FUNCTIONS
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
def battle(enemy_type):
    global inventory
    global animals
    global animals_ind
    fight = True
    choices = ('bite','claw', 'dodge')
    user_success = False
    enemy_success = False
    enemy_health = 100
    user_health = 100
    user_ap = 2.5
    enemy_ap = 2.5

    while fight == True:

        allowed_response = False

        print("\n")
        clearConsole()

        if enemy_ap < 0.5: #RESET THE ATTACK POWER IF IT GOES BELOW 0.5
            enemy_ap = 0.5
        if user_ap < 0.5:
            user_ap = 0.5

        if enemy_health <1 and user_health>0:
            fight == False
            print(f"\nWhat a battle! {your_name} defeated the {enemy_type}!")
            input("\n(press enter)\n")
            if enemy_type == 'badger':
                #GO SOMEWHERE ELSE ON THE TREE
                typewrite(f"Worn out by the ordeal, {your_name} staggers through the forest, lost, unknowingly going round and round the forest in circles! ")
                input ("(press enter)")
                A5()
                return
            elif enemy_type == 'feral cat':
                #GO SOMEWHERE ELSE ON THE TREE
                typewrite(f"Worn out by the ordeal, {your_name} staggers through the ally until eventually it leads out onto a street \n\n- a very familiar road - {your_name} made it!\n")
                input("Now, you can go home! At last! (press enter)")
                game_win()
                return
            elif enemy_type == 'dog':
                input("Now, you can go home! At last! (press enter)")
                game_win()
                return

        elif user_health <1:
            fight == False
            animals.pop(0)
            animals.insert(0,"")
            animals_ind.pop(0)
            animals_ind.insert(0,"")
            print(f"{your_name} was defeated by the {enemy_type}.")
            input("(Press enter)")
            print(f"\n{your_name} begins to lose conciousness.")
            print("""
                __..--''``---....___   _..._    __
      /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
    ///_.-' _..--.'_    \                    `( ) ) // //
    / (_..-' // (< _     ;_..__               ; `' / ///
    / // // //  `-._,_)' // / ``--...____..-' /// / //
        """)
            print(f"\nDazed and confused, {your_name} wakes up back at the trash site.")
            input("\n(press enter)")
            fight == False
            animals.pop(0)
            animals.insert(0,"")
            animals_ind.pop(0)
            animals_ind.insert(0,"")
            start_game()

        print(f"{your_name.upper()}'S ATTACK POWER: ", end = "")
        for i in range(int(user_ap*10-2/4)): print(">", end = "")
        print(f"\n{enemy_type.upper()}'S ATTACK POWER: ", end = "")
        for i in range(int(enemy_ap*10-2/4)): print(">", end = "")

        print(f"\n{your_name.upper()}'S HEALTH: {user_health}/100\n{enemy_type.upper()} HEALTH: {enemy_health}/100")
        print("(1) Bite                  (2) Claw                                (3) Dodge ".center(150))
        print("""                                - a very powerful          - a weaker attack but may              - a chance to avoid the attack
                                   strong attack               increase overall attack power           and increase attack power
        """)
        
        while allowed_response == False:
            user_sel = input("                                    : ")
            print("\n")
            if user_sel == '1' or user_sel == '2' or user_sel == '3':
                allowed_response = True
                user_sel = int(user_sel)-1
            else:
                print("\bYou must select a valid option! (1), (2) or (3)\n")

        enemy_sel = random.randint(0,2)
        print(f"{your_name} tries to {choices[user_sel]} the {enemy_type}!")
        input("(press enter)")
        print(f"\nThe {enemy_type} tries to {choices[enemy_sel]} {your_name}!")
        input("(press enter)")
        enemy_success = random.randint(1,10)
        user_success = random.randint(1,10)

        if enemy_sel == 2 and user_sel == 2: #Both try to dodge
            print(f"""\nBoth dodged!

        {your_name}'s attack power decreases.
        The {enemy_type}'s attack power decreases.""")
            user_ap -=.5 #enemy attack power decreases
            enemy_ap -=.5 #enemy attack power decreases
        

        elif enemy_sel == 2: #enemy tries to dodge
            if user_sel == 1 or user_sel == 0:

                if enemy_success > user_success:
                    print(f"\nThe {enemy_type} attempts to {choices[enemy_sel]} and succeeds! {your_name}'s attack power decreases.")
                    #enemies dodge successful
                    user_ap -=1 #users attack power decreases
                
                elif enemy_success < user_success:
                    print(f"\nThe {enemy_type} attempts to {choices[enemy_sel]} you but fails!")

                    #IF USER ATTACK WAS CLAW, perform a smaller attack and grant ap
                    if user_sel == 1:
                        damage = random.randint(1,10)*user_ap
                        print(f"{your_name}'s {choices[user_sel]} attack inflicts {damage} damage on the {enemy_type}!")
                        print(f"{your_name}'s attack power increases!")
                        user_ap += .5
                        enemy_health -= damage
                    #IF USER ATTACK WAS BITE, perform a bigger attack
                    elif user_sel == 0:
                        damage = random.randint(5,15)*user_ap
                        print(f"{your_name}'s {choices[user_sel]} attack inflicts {damage} damage on the {enemy_type}!")
                        enemy_health -= damage

                else:
                    print(f"\nThe {enemy_type} attempts to {choices[enemy_sel]} {your_name} and fails. But {your_name}'s {choices[user_sel]} also fails!")

        elif user_sel == 2: #user tries to dodge
            if enemy_sel == 1 or enemy_sel == 0:

                if enemy_success < user_success:
                    print(f"\n{your_name} attempts to {choices[user_sel]} the {enemy_type}'s {choices[enemy_sel]} attack and succeed! The {enemy_type}'s attack power decreases.")
                    #users dodge sucessful
                    enemy_ap -=1 #enemies attack power decreases
                
                elif enemy_success > user_success:

                    print(f"\n{your_name} attempts to {choices[user_sel]} the {enemy_type} but it fails!")

                #IF ENEMY ATTACK WAS CLAW, perform a smaller attack and grant ap
                    if enemy_sel == 1:
                        damage = random.randint(1,10)*enemy_ap
                        print(f"The {enemy_type}'s {choices[enemy_sel]}'s attack inflicts {damage} damage on {your_name}!")
                        print(f"The {enemy_type}'s attack power increases!")
                        enemy_ap += .5
                        user_health -= damage
                #IF ENEMY ATTACK WAS BITE, perform a bigger attack
                    elif enemy_sel == 0:
                        damage = random.randint(5,15)*enemy_ap
                        print(f"The {enemy_type}'s {choices[enemy_sel]}'s attack inflicts {damage} damage on {your_name}!")
                        user_health -= damage
                else:
                    print(f"\n{your_name} attempts to {choices[user_sel]} the {enemy_type} and fail. But the {enemy_type}'s {choices[enemy_sel]} attempt also fails!")

        if user_sel != 2 and enemy_sel != 2: #IF BOTH ARE TRYING TO ATTACK
            print("\n")

            if user_success > 5:
                if user_sel == 0: #user tries to bite
                    damage = random.randint(5,15)*user_ap
                    print(f"{your_name}'s {choices[user_sel]} attack inflicts {damage} damage on the {enemy_type}!")
                    enemy_health -= damage

                elif user_sel == 1: #user tries to claw
                        damage = random.randint(1,10)*user_ap
                        print(f"{your_name}'s {choices[user_sel]} attack inflicts {damage} damage on the {enemy_type}!")
                        print(f"{your_name}'s attack power increases!")
                        user_ap += .5
                        enemy_health -= damage
            else:
                print(f"{your_name}'s {choices[user_sel]} attack failed!")
            
            if enemy_success > 5:
                if enemy_sel == 0: #enemy tries to bite
                    damage = random.randint(5,15)*enemy_ap
                    print(f"The {enemy_type}'s {choices[enemy_sel]}'s attack inflicts {damage} damage on {your_name}!")
                    user_health -= damage

                elif enemy_sel == 1: #enemy tries to claw
                    damage = random.randint(1,10)*enemy_ap
                    print(f"The {enemy_type}'s {choices[enemy_sel]}'s attack inflicts {damage} damage on {your_name}!")
                    print(f"The {enemy_type}'s attack power increases!")
                    enemy_ap += .5
                    user_health -= damage
        
            else:
                print(f"The {enemy_type}'s {choices[user_sel]} attack failed!")
        input("\n(press enter)")
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def typewrite(words):
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

#SPECIAL ROOM FUNCTIONS
def intro():
    global your_name
    clearConsole()
    typewrite("\n\nThrough the game, you will be presented with a series of choices. Usually these choices will be numbered.\n")
    typewrite("\nYou must type the number of the choice you'd like to follow.\n")
    typewrite("\nPay attention to the options and choose wisely. Your character's fate depends on it.\n\n")

    print(colored(0,255,0,"\n(1) Start game      (2) Quit\n"))
    answer = input(colored(0,255,0,": "))
    if answer == "1":
        clearConsole()
        print("""
   _.---.._             _.---...__
.-'   /\   \          .'  /\     /
`.   (  )   \        /   (  )   /
  `.  \/   .'\      /`.   \/  .'
    ``---''   )    (   ``---''
            .';.--.;`.
          .' /_...._\ `.
        .'   `.a  a.'   `.
       (        \/        )
        `.___..-'`-..___.'
           \          /
            `-.____.-'
        """)
        your_name = input(colored(0,255,0,"\nEnter your characters name: ")).capitalize()
        if your_name == "Code nation" or your_name == "Python":
            clearConsole
            typewrite("\nHey. Pssssst. HEY!")
            typewrite("\n\nYou there. Yes you!")
            typewrite("\n\nShhhhh. Keep it down. I'm just here to tell you, you found a secret room!\n\nPretty cool huh?")
            input("\n\n(press enter!)")
            print("""
                
                      .===========.
                      | print(    |
                      |  "Hello   | 
            `,        |  world!") |
            {         |___________|
            )         |_________-_|_,-.
           ___'      [_____________]   )
          ((  |     |\---/|  / ),,,.  (_  
        ---|__|----/;     |-/ /, ,,,\ (>`\ 
                  (_)     (' /-._____) \__)
       ============(       ,'==========
        ||   _     |      |
        || o/ )    |      | o
        || ( (    /       ;
        ||  \ `._/       /
        ||   `._        /|
        ||      |\    _/||
      __||_____.' )  |__||____________
       ________\  |  |_________________
                \ \  `-.
            """)
            input(colored(100, 100, 255,"\n[TAKE COFFEE]"))
            inventory.append("Coffee")
            input(colored(100, 100, 255,"\n[Coffee] added to inventory. (press enter)"))
            print(colored(100, 100, 255,f"Inventory: {inventory}"))

            input(colored(100, 100, 255,"\n[TAKE COMPUTER CHIP]"))
            inventory.append("Computer chip")
            input(colored(100, 100, 255,"\n[Computer chip] added to inventory. (press enter)"))
            print(colored(100, 100, 255,f"Inventory: {inventory}"))
            your_name = input(colored(0,255,0,"\n\nNow. Enter your REAL name: ")).capitalize()
            
    else:
            print ("\nYour loss! Maybe tomorrow.")
            return
            
    #Title Card
    clearConsole()
    print ("""
       ______      __           __               __     ____         __  __            _______ __       
      / ____/___ _/ /__        / /   ____  _____/ /_   /  _/___     / /_/ /_  ___     / ____(_) /___  __
     / /   / __ `/ __(_)  O   / /   / __ \/ ___/ __/   / // __ \   / __/ __ \/ _ \   / /   / / __/ / / /
    / /___/ /_/ / /__        / /___/ /_/ (__  ) /_   _/ // / / /  / /_/ / / /  __/  / /___/ / /_/ /_/ / 
    \____/\__,_/\__(_)  O   /_____/\____/____/\__/  /___/_/ /_/   \__/_/ /_/\___/   \____/_/\__/\__, /  
                                                                                               /____/   
                    *
                 __                 *
              ,db'    *        *
            ,d8/           *        *    *
            888
            `db\       *     *
               `o`_                    *    *
         *               *   *    _      *
               *                 / )
            *    (\__/) *       ( (  *
          ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
         | @|  ={      }= | @|  / / | @|o |
        _j__j__j_)     `-------/ /__j__j__j_
        ________(               /___________
        |  | @| \              || o|O | @|
        |o |  |,'\       ,   ,'"|  |  |  |
        vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
                   _) )    `. \ /
                  (__/       ) )
                            (_/
    """)
    #Setting scene
    input ("Welcome to the adventure. (press enter to begin)")
    clearConsole()
    typewrite(f"\n{your_name} the cat wakes up startled. Surrounded by trash, illumated by the bright overhead lighting of a trash dump.\n\n")
    typewrite(f"{your_name}, is a cat well renouned for sleep walking, often knocking over the pots and pans in the kitchen and waking everyone in the house up, or even ending up passed out in the yard! This time however, the sleepwalking has literally gone a little too far, and upon waking up all {your_name} can see and smell, is piles upon piles of trash bags. {your_name} has somehow sleep walked to a trashyard on the other side of town! \n\n")
    typewrite(f"{your_name} gets up and begins to look around. Immediately anxious about how to get back home. \n\n")
    input("(press enter)")
    
    start_game()
def start_game():
    if animals[0] == "" and animals[1] == "" and animals[2] == "":
        lose_game()

    typewrite(f"\nGlancing around, {your_name} notices various animals all going about their business. Maybe one of them can help?")
    if animals[0] != "" and animals[1] != "" and animals[2] != "": #IF ALL ANIMALS ARE PRESENT XXX
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|\_/|,,_____,~~`\                   \__|____|____|____|____|____|___
    ____|___(.".)~~     )`~}}\                   \___|____|____|_         ____|_
    __|____|_\o/\ /---~\\\\ ~}}_\                   \|____|____|   (\.-./)  _|____
    ____|____|___//    _// ~}_|\                   \__|____|_  =  (^Y^) =  __|
    __|____|___/-------------------------------------___|____|__ __|-`\/____|___
    ____|____//---------------//                  / |_|____|____|__U_|U__ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |      _    ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |     (o>   |___|__| | | | |__|_____|___
    |--------------         ------------|   _-`__)  ||_____| | | | |_____|____|__
    |                                   |   /_/_/'  |___|__| | | | |__|_____|___ |
    ---------------------------------------//--|_---|______|_______|_____|____|__
    """)

    if animals[0] == "" and animals[1] != "" and animals[2] != "": #PIGEON IS NOT THERE BUT OTHERS ARE 0XX
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|\_/|,,_____,~~`\                   \__|____|____|____|____|____|___
    ____|___(.".)~~     )`~}}\                   \___|____|____|_         ____|_
    __|____|_\o/\ /---~\\\\ ~}}_\                   \|____|____|   (\.-./)  _|____
    ____|____|___//    _// ~}_|\                   \__|____|_  =  (^Y^) =  __|
    __|____|___/-------------------------------------___|____|__ __|-`\/____|___
    ____|____//---------------//                  / |_|____|____|__U_|U__ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |           ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |           |___|__| | | | |__|_____|___
    |--------------         ------------|           ||_____| | | | |_____|____|__
    |                                   |           |___|__| | | | |__|_____|___ |
    ------------------------------------------------|______|_______|_____|____|__
    """)

    if animals[0] == "" and animals[1] == "" and animals[2] != "": #IF PIGEON AND FOX ARE NOT THERE BUT RAT IS 00X
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|___|____|___|__\                   \__|____|____|____|____|____|___
    ____|____|____|____|___|_\                   \___|____|____|_         ____|_
    __|____|____|___|____|___|\                   \|____|____|   (\.-./)  _|____
    ____|____|____|____|____|__\                   \__|____|_  =  (^Y^) =  __|
    __|____|___/-------------------------------------___|____|__ __|-`\/____|___
    ____|____//---------------//                  / |_|____|____|__U_|U__ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |           ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |           |___|__| | | | |__|_____|___
    |--------------         ------------|           ||_____| | | | |_____|____|__
    |                                   |           |___|__| | | | |__|_____|___ |
    ------------------------------------------------|______|_______|_____|____|__
    """)

    if animals[0] != "" and animals[1] == "" and animals[2] != "": #IF PIGEON AND RAT IS PRESENT BUT FOX IS GONE XOX
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|___|____|___|__\                   \__|____|____|____|____|____|___
    ____|____|____|____|___|_\                   \___|____|____|_         ____|_
    __|____|____|___|____|___|\                   \|____|____|   (\.-./)  _|____
    ____|____|____|____|____|__\                   \__|____|_  =  (^Y^) =  __|
    __|____|___/-------------------------------------___|____|__ __|-`\/____|___
    ____|____//---------------//                  / |_|____|____|__U_|U__ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |      _    ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |     (o>   |___|__| | | | |__|_____|___
    |--------------         ------------|   _-`__)  ||_____| | | | |_____|____|__
    |                                   |   /_/_/'  |___|__| | | | |__|_____|___ |
    ---------------------------------------//--|_---|______|_______|_____|____|__
    """)

    if animals[0] != "" and animals[1] != "" and animals[2] == "": #IF PIGEON AND FOX IS PRESENT BUT RAT IS GONE XX0
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|\_/|,,_____,~~`\                   \__|____|____|____|____|____|___
    ____|___(.".)~~     )`~}}\                   \___|____|____|_         ____|_
    __|____|_\o/\ /---~\\\\ ~}}_\                 \|____|____|            _|____
    ____|____|___//    _// ~}_|\                   \__|____|_              __|
    __|____|___/-------------------------------------___|____|__ ___________|___
    ____|____//---------------//                  / |_|____|____|____|___ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |      _    ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |     (o>   |___|__| | | | |__|_____|___
    |--------------         ------------|   _-`__)  ||_____| | | | |_____|____|__
    |                                   |   /_/_/'  |___|__| | | | |__|_____|___ |
    ---------------------------------------//--|_---|______|_______|_____|____|__
    """)

    if animals[0] == "" and animals[1] != "" and animals[2] == "": #IF PIGEON AND RAT ARE GONE, BUT FOX IS PRESENT 0X0
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|\_/|,,_____,~~`\                   \__|____|____|____|____|____|___
    ____|___(.".)~~     )`~}}\                   \___|____|____|_         ____|_
    __|____|_\o/\ /---~\\\\ ~}}_\                 \|____|____|            _|____
    ____|____|___//    _// ~}_|\                   \__|____|_              __|
    __|____|___/-------------------------------------___|____|__ ___________|___
    ____|____//---------------//                  / |_|____|____|____|___ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |           ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |           |___|__| | | | |__|_____|___
    |--------------         ------------|           ||_____| | | | |_____|____|__
    |                                   |           |___|__| | | | |__|_____|___ |
    ------------------------------------------------|______|_______|_____|____|__
    """)

    if animals[0] != "" and animals[1] == "" and animals[2] == "": #X00 IF PIGEON IS PRESENT, BUT FOX AND RAT ARE GONE
        print("""\n
        ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
    __|_____|___|____|___|__\                   \__|____|____|____|____|____|___
    ____|____|____|____|___|_\                   \___|____|____|_         ____|_
    __|____|____|___|____|___|\                   \|____|____|            _|____
    ____|____|____|____|____|__\                   \__|____|_              __|
    __|____|___/-------------------------------------___|____|__ ___________|___
    ____|____//---------------//                  / |_|____|____|____|___ |____|
    __|____//               //                  / __|___|____|____|____|____|____|
    ____|//               //                  / /  |||____|____|____|____|____|_
    __|//               //                  / /    ||___|____|____|____|____|___
    _//_______________//   o o            / /      |||____|___/-\___|____|____|__
    ------------------------------------/   ------- |___|_|---------|__|____|____|
    | DO NOT PLAY |         | HOUSEHOLD |      _    ||_____| | | | |_____|____|_
    | ON OR AROUND|         |WASTE ONLY |     (o>   |___|__| | | | |__|_____|___
    |--------------         ------------|   _-`__)  ||_____| | | | |_____|____|__
    |                                   |   /_/_/'  |___|__| | | | |__|_____|___ |
    ---------------------------------------//--|_---|______|_______|_____|____|__
    """)

    print(colored(0,255,0,f"\n\n\nWho should {your_name} approach?\n"))
    print(colored(0,255,0,f"{animals_ind[0]} {animals[0]}          {animals_ind[1]} {animals[1]}           {animals_ind[2]} {animals[2]}".center(150)))
    
    while True:
        answer = input(colored(0,255,0,"\n%52s: ")%" ")
        if answer.isdigit() == True:
            answer = int(answer)

            if animals[answer-1] != "":
                if answer == 1:
                    A1() #PIGEONSTART
                    return
                elif answer == 2:
                    B1() #FOXSTART
                    return
                elif answer == 3:
                    C1() #RATSTART
                    return
                    
            else:
                print(colored(255, 0, 0,"You must select a valid option"))
                continue 
        else:
            print(colored(255, 0, 0,"You must select a valid option"))
            continue
def lose_game():
    print("""\n
    ____|____|____|____|____|____|____|____|____|____|____|____|____|____|____|_
__|_____|___|____|___|__\                   \__|____|____|____|____|____|___
____|____|____|____|___|_\                   \___|____|____|_         ____|_
__|____|____|___|____|___|\                   \|____|____|            _|____
____|____|____|____|____|__\                   \__|____|_              __|
__|____|___/-------------------------------------___|____|__ ___________|___
____|____//---------------//                  / |_|____|____|____|___ |____|
__|____//               //                  / __|___|____|____|____|____|____|
____|//               //                  / /  |||____|____|____|____|____|_
__|//               //                  / /    ||___|____|____|____|____|___
_//_______________//   o o            / /      |||____|___/-\___|____|____|__
------------------------------------/   ------- |___|_|---------|__|____|____|
| DO NOT PLAY |         | HOUSEHOLD |           ||_____| | | | |_____|____|_
| ON OR AROUND|         |WASTE ONLY |           |___|__| | | | |__|_____|___
|--------------         ------------|           ||_____| | | | |_____|____|__
|                                   |           |___|__| | | | |__|_____|___ |
------------------------------------------------|______|_______|_____|____|__
""")
    typewrite(f"\n{your_name} returns to the dumpsite, but nobodies around... I guess this is {your_name}'s new home now...")
    input("(Press enter)")
    clearConsole
    print("""
       ________________   ___/-\___                   ___/-\___
     / /             ||  |---------|                 |---------|
    / /              ||   | | |   |                   |   |   |
   / /             __||   | | | | |        ^~^  ,     | | | | |
  / /   \\        I  ||   |   | | |       ('Y') )     | | | | |
 (-------------------||   | | | | |       /   \/      | | | | |
 ||               == ||   |_______|      (\|||/)      |_______|
 ||   C-N TRASH INC  | =============================================
 ||          ____    |                                ____      |
( | o      / ____ \                                 / ____ \    |)
 ||      / / . . \ \                              / / . . \ \   |
[ |_____| | .   . | |____________________________| | .   . | |__]
          | .   . |                                | .   . |
           \_____/                                  \_____/
    """)
    typewrite(f"\nOn your travels, you found a total of {inventory.len()} out of a possible 4 items.")
    if len(inventory) > 0:
        print("\n",inventory,"\n\n\n")
    input("(press enter to exit the game)")
def game_win():
    input("\nThere it is! Home! You actually made it! (press enter)")
    print("""                                                          ______________
                                                         |##############
              __             __                          |##############
_____________|  |_____     _(   )                        |##############
UUUUUUUUUUUUU|__|UUUUU| ,-'      )_                      |##############
UUU_UUUUUU_UUUUUU_UUUU|(   (  /    )                     |   __   __   _
UU|_|UUUU|_|UUUU|_|UUU|.  \   )  _) )                    |  |  | |  | | 
UUUUUUUUUUUUUUUUUUUUUU| `.  .    )  )                    |  |__| |__| |_
======================|(_   |  )  _)                     |
     __     __    __  |(__(_|____)_______________________|   __   __   _
|   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuuuu,'.uuu|  |  | |  | | 
|   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuu,'   `.u|  |__| |__| |_
======================|uuuu_uuuuuu_uuuuuu_uuuuu,'__   __`.
     __     __    __  |uuu| |uuuu| |uuuu| |uuuu||  | |  ||   __   __   _
|   |__|   |__|  |__| |uuu|_|uuuu|_|uuuu|_|uuuu||__| |__||  |  | |  | | 
|   |__|   |__|  |__| |=_====__================'         |  |__| |__| |_
======================||  | |  |  __   __   __   __   __ |______________
  ___  __    ________ ||__| |__| |  | |  | |  | |  | |  ||+++++++++++++_
||_|_||  |  |  |     || _______  |__| |__| |__| |__| |__||++.-------.+| 
||_|_||- |  | -|     |||   |   |                         |++|   |   |+|_
 |_|_||  |  |  |_____|||   |o  |  _     ____________  _  |++|   |-  |+++
---. _|--|__|--|_____|||===|   |_|_|_  /_|__|_______| _|_|++|___|___|+++
----`. ___             ;---'---'      |  |_-|       |__     |       \   
--(_)-'_ _\___________/________|____/_'-(_)-----(_)-' _\____|________\__
____________________________________________________________________""")

    print(colored(0,255,0,"\n(1) [ENTER THE HOUSE]              (2) [STAY A STRAY]"))
    answer = input(colored(0,255,0,": "))
 
    while True:
        if answer != '1':
            print(f"\n{your_name} went though all of that for nothing? Are you absolutely sure?\n\n")
            print(colored(0,255,0,f"(1) NO I DON'T MEAN IT! TAKE ME HOME!         (2) {your_name} prefers this new life living wild and free.\n"))
            answer = input(colored(0,255,0,": "))
            input("\nOkay... (Press enter)")
            if answer != '1':
                lose_game()
                return
            else:
                break
        break

    print("""\n
 ________________________________________________________________________
|: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|__________ : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :|
|__]\\\% \% \% | : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|___]\\\% \% \%|: :______ : : : : : : : : : : : : : : : : : : : : :___: : : :|
|____]\% \% | :|======| :_: : : : : : . : : : : : :_: : : : : :/   \: : : |
|_____]\\\% \%|: ||\|||||:/_\: :,: : :.'o'.: : :,: :/_\: : : : :|//   |: : :|
|______]\% | :|======| =|= __#_____|___|_____#__ =|= : : : : | ,*, | : : |
|_______]\%|: |______|: ^ :[___]           [___]: ^ : : : : : \*;*/ : : :|
|________]\| :|__  __| : : [_|_] o  `(,  o [_|_] : : : : :_____(_)_____: |
|_________]\: | .||. |: : :[___] |  ( )  | [___]: : :_!_: ||   .|.   || :|
|__________]==|__||__|====_[_|_]/!\_@@@_/!\[_|_]_===/___\=||____|____||==|
|                         '====================='     |_                 |
     _                             c^\___             |( |               |
    |_)         __.;;.__           _\|_\`)__         _|_)|               |
    /_\__      / ;(;;); \     _______________                            |
  ~=_|_ _)====/__________\== (               )====================~      |
 ~=|___|LL====|==========|= (\               /)====================~     |
~============================|_______________|======================~    |
=============================LLLLLLLLLLLLLLLLL=======================~   |
++====================================================================~  '
""")

    typewrite(f"On your travels, you found a total of {len(inventory)} out of a possible 4 items.\n")
    if len(inventory) > 0:
        input("(press enter)")
        print("\n",inventory,"\n\n\n")
    input("(press enter to exit the game)")

#A / PIGEON PATH
def A1():
    typewrite(f"\n{your_name} carefully approaches the pigeon, who seems too distracted to notice. {your_name} sits for a moment, observing him as he pecks redundantly at the bare ground.")
    typewrite(f"\n\n**{your_name.upper()}'S STOMACH GRUMBLES LOUDLY**")
    typewrite(f"\n\nThe pigeon frantically looks up at the cat stood before him, a startled look in his eyes.\n")
    print("""
                          .---.       __________________________________________________________________________
                         /  (o \_    /                                                                       \\
                         | -='.'"` ＜ 'Oh. H.. He.. Hello.. You're... not going t.. to eat me are you?        |
                     _.=`     \\      \\   I'm sure I can help you with something if you'll only spare me...'   /
                 _.=`.   -.    |      \\______________________________________________________________________/
            .===:._ ' '.   ;   |     
 ________,.='`^~""``"====-'   ,'     
'-========-""'"-=..,,,_____,.'
                      `\ `\\
                     ,-'==,\ """)

    print("                          ,-`==;",(colored(0, 255, 0,"         (1) Make friends      (2) Attack the pigeon \n")))
    while True:
        answer = input(colored(0, 255, 0,"                                          : "))
        if answer == '1':
            A2()
        elif answer == '2':
            A3()
        else:
            print(colored(255, 0, 0,"You must select a valid option."))
            continue
def A2():
    typewrite(f"""\nAmused, {your_name} smiles whilst casually licking between the pawpads. 'No. I'm not going to eat you.'\n
The pigeon releases a sigh of relief. 'Oh, thank-coo!'\n
'You.. could help me though' you say. The cat's gaze wanders longlingly over the horizon. 'I'm looking for somewhere'.\n
'Where?' says the pigeon?\n
'Home...' {your_name} mutters.\n 
'Well... where's home exactly?' the pigeon prompts. 'Can you describe it?'\n
""")
    answer = False
    while answer != '3':

        print(colored(0, 255, 0,"(1) Metalic monsters       (2) Bright orbs       (3) Giant zooming snakes\n".center(150)))
        answer = input(colored(0, 255, 0,"                                      : "))
        if answer == '1':
            print('''
    ________/""||"""""""""""""|_________/""||"""""""""""""|_________/""||"""""""""
    .._/"\_, |  ||_____________| ._/"\_, |  ||_____________| ._/"\_, |  ||_________
    "o---o" 'O--OO       OO OO  "o---o" 'O--OO       OO OO  "o---o" 'O--OO       O
    """"\,   .__/""\__,   .__/"""""\,   .__/""\__,   .__/"""""\,   .__/""\__,   ._
    ---()"   "()----()"   "()-----()"   "()----()"   "()-----()"   "()----()"   "(
    \                 /"""T"""\                 /"""T"""\                 /"""T"""
    _>---\       ,---<____|____>---\       ,---<____|____>---\       ,---<____|___
    -/"\ {      / /"\    -|   -/"\ {      / /"\    -|   -/"\ {      / /"\    -|
    -\_/-=      =-\_/-----+----\_/-=      =-\_/-----+----\_/-=      =-\_/-----+---
    ______________________________________________________________________________
    ''')
            input("'Let's see... there's a thundering path with shiny metalic monsters..' (press enter)")
            typewrite("\n'You're talking about cars - they're everywhere. I'm gonna need more than that...' the pigeon advises. \n\n")

        if answer == '2':
            print("""
               ()                                                ()
             ()\/()                                            ()\/()
            ._\()/_.                                          ._\()/_.
               ||                                                ||
               ||                                                ||
               ||                                                ||
               ||                                                ||
               ||                                                ||
               ||                                                ||
               ||                                                ||
               ||________________________________________________||
               ||/_____/_____/_____/_____/_____/_____/_____/____\||
               ''''''''''''''''''''''''''''''''''''''''''''''''''''
""")
            input("'Ummm.. okay.. how about this. On every path corner, there is a glowing sun!' (press enter)")
            typewrite("\nThe pigeon stares blankly. 'You must mean streetlamps..?' Can you think of anything else more specific?\n\n")
    print("""   _____                 . . . . . o o o o o
  __|[_]|__ ___________ _______    ____      o
 |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
_|________|_[_________]_[________]_|__|________)<
  oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    print("""Hm.. Well there are these long metalic snakes that make a lot of noise, and go past all day long.\n""")
    input("(press enter)\n")
    typewrite("""The pigeon perks up.. 'Wait you.. live near the train station? Why didn't you just say! I fly over there all the time, I know exactly where that is! -

By paw, there's two ways you could go.. If you head out of here and go straight on you'll come to an alleyway, follow that around and you'll arrive at the station. It's quite a long way though and there's some dodgey characters around. Alternatively you could take a shortcut through the river just over there. You'll have to get wet and try to swim, it's a little risky, but you'll reach home much sooner if you manage it.'\n\n""")
    print(colored(0, 255, 0,"(1) Go through the dark scary alleyway        (2) Take a shortcut through the treacherous river".center(150)))
    while True:
        answer = input("\n%27s: " %" ") 
        if answer == '1':
            A4()
        elif answer == '2':
            A5()
        else:
            print(colored(0, 255, 0,"You must select a valid option."))
            continue
def A4():
    global inventory
    typewrite(f"\n{your_name} thanks the pigeon and leaves. It doesn't take long to find the alleyway entrance. {your_name} enters hesitantly.\n")
    print("""
                 / _     /  /    /.::::::::.\ \   \ \     _ \\
                /_(_)___/ /   / /.::::::::::.\   \   \___(_)_\\
---------------/  / \  /   /   /.::::::::::::.\  \ \  \  / \  \-------
______________/_______/  / /  /.::::::;;::::::.\ \     \_______\________
|       |     [===  =] /   / /.::::::;;;;;:::::.\   \ \ [==  = ]   |
|_______|_____[ = == ]/  /  /.::::::;;;;;;::::::.\  \  \[ ===  ]___|____
     |       |[  === ] /   /.::::::;;;:;;;:::::::.\   \ [=  ===] |
_____|_______|[== = =]/   /.::::::;;;:::;;;:::::::.\   \[ ==  =]_|______
 |       |    [ == = ] / /.:::::::;;::::;;;::::::::.\ \ [== == ]      |
_|_______|____[=  == ]/ /.:::::::;;::::::;;;::::::::.\ \[  === ]______|_
   |       |  [ === =] /.:::::::;;:::::::;;;:::::::::.\ [===  =]   |
___|_______|__[ == ==]/.:::::::;;;::::::::;;;:::::::::.\[=  == ]___|_____
""")
    typewrite(f"{your_name} wanders through the alleyway for what seems like hours. The sun begins to set, and it soon gets darker, and darker. With only flickers of moonlight for company, under the shade of impsosing brick layered walls, {your_name} can barely see.")
    input(f"\n\n{your_name} finds some [catnip] (press enter)")
    print("""
        W
       WWW
       WWW
      WWWWW
W     WWWWW     W
WWW   WWWWW   WWW
 WWW  WWWWW  WWW
  WWW  WWW  WWW
   WWW WWW WWW
     WWWWWWW
  WWWW  |  WWWW
        |
        |""")
    input(colored(100, 100, 255,"\n[TAKE CATNIP]"))
    inventory.append("Catnip")
    input(colored(100, 100, 255,"\n[Catnip] added to inventory. (press enter)"))
    print(colored(100, 100, 255,f"Inventory: {inventory}"))
    typewrite(f"\n{your_name} soon begins to hear noises.. shuffling...")
    input("....... (Press enter)")
    print('''
    
                  ,_> `.   ,';
             _,-`'      `'   '`'...._
            / \`\                /./\\\\__                      ____________________________
           (   \  `.,`~ \~'-. ,' ,'  ) _\\\\                  /   OI .... !                 |
            \   \ ,'  ') )   `. /   /    <,.               /    THAT       /`\ /`\  ,---  |
          \ ,'    ( /      `.  /   /  `-,                 |     BELONGS   |   |   | |---  |
         `.,'     `         `.,'  `\   ,-  `-._          /      TO        |   |   | |___  |
          ,'   /   ,,,      ,,,     \     `-.          ,'   ______________________________|
         ,'     ____ \    / ____ `     ; `. `(`-\\\\   .'___-'
                  `(o\|   |/o)'      ;     `'`,    ___ 
      ,-'    \      '  ___    `      /     \ <_   ',  `\\\\
     `-._;  ,' |  .::. *.*' :.. |       `-.    _\  |    : 
       _/        /`-..-'^`-..-'\ `.        \,-'    _`.   '\\
       >_ /     ;  (\/( ' )\/)  ;     `-.  _<    /"       .
       ,-'          .\`^^^'/,'        \ _<_____-'    ,---'
        `-,  ,'     `.`"""','   `-.   <`'           /
          | '._         '`'   \       < \_______..-'
         /     >   ,'       ,   `-.   <`'\\\\
        |       `,/          \      ,-`   |
        \ | | /  `,   ,' |   /     /\ | | /
         `'`'"                       `"'`' 
    ''')
    typewrite(f"""A fierce looking wildcat leaps toward {your_name}. There is no time to react, before {your_name} is pinned violantly to the ground.
""")
    input("\n(press enter)")
    battle("feral cat")
def A5():
    typewrite(f"\n{your_name} heads towards the sound of rushing water and soon comes accross a wide river. It's a little ferocious but there is no other way to cross it. {your_name} will just have to swim. It's not going to be fun.")
    typewrite(f"\n\n{your_name} will have to swim extremely carefully to get accross.\n")
    input("\nAre you ready? (press enter to begin)")
    clearConsole()
    order_options = ["rides the rapid","holds back","kicks hard","dives"]
    correct_order = (order_options[random.randint(0,3)],order_options[random.randint(0,3)],order_options[random.randint(0,3)],order_options[random.randint(0,3)])
    order_solved=False
    typewrite(f"You must help {your_name} swim accross the river in a particular way - otherwide, the rapids will surely sweep the cat back to shore! ")
    while order_solved == False:
        print("""\n
   #@@@&                            (|  |)                               
  &@@@@@%\%                    -    /^-^\              ,#@@..     #@        -          
 ,&&@@@@@@'        ^              _-(o.o)-_  -        #@@@&@%\%   @&@%                 
   `|||'         -                  || ||             &@@@@@%\%   '@@"           -         
 -  |||    ^                       ^"   "              `|||'   ^   ||       -             
    /|\                    -                            /|\           ^   
_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,~~-.~~~~..,,,_,__.~~~~~,--.~~~~~..,,,_,_
                                                                    
         ~~                                                                         
                                ~                   ~                    ~
  ~                ~~~                                                        
                                                                ~~         
         ~      ~~                              ~                            
                                                                              
~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----
                                                                             
          ^  -                              -                              -          
        """)

        answer = input (colored(0, 255, 0,"(1) Ride the rapid    (2) Hold back     (3) Kick hard     (4) Dive under\n\n: "))
        if answer != "1" and answer != "2" and answer != "3" and answer != "4":
            clearConsole()
            print(colored(255, 0, 0,f"The current pulls {your_name} back, because you must enter a valid answer (1), (2), (3) or (4)"))
            continue
        answer = int(answer)-1

        if order_options[answer] == correct_order[0]:
            clearConsole()
            print(f"""{your_name} sucessfully {order_options[answer]}.\n
   #@@@&                              n                            
  &@@@@@%\%                    -      ||               ,#@@..     #@        -          
 ,&&@@@@@@'        ^                ./||\,   -        #@@@&@%\%   @&@%                 
   `|||'         -                  (|  |)            &@@@@@%\%   '@@"           -         
 -  |||    ^                       ^/^-^\              `|||'   ^   ||       -             
    /|\                    -      _-(o.o)-_             /|\           ^   
_,__.~~~~~,_,.----~~~,_,.---.~~~~~.'|| ||`~~~..,,,_,__.~~~~~,--.~~~~~..,,,_,_
                                    "   "                           
         ~~                                                                         
                                ~                   ~                    ~
  ~                ~~~                                                        
                                                                ~~         
         ~      ~~                              ~                            
                                                                              
~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----
                                                                             
          ^  -                              -                              -  
            """)
 
            answer = input (colored(0, 255, 0,"(1) Ride the rapid    (2) Hold back     (3) Kick hard     (4) Dive under\n\n: "))
            if answer != "1" and answer != "2" and answer != "3" and answer != "4":
                clearConsole()
                print(colored(255, 0, 0,"The current pulls you back, because you must enter a valid answer (1), (2), (3) or (4)"))
                continue
            answer = int(answer)-1

            if order_options[answer] == correct_order[1]:
                clearConsole()
                print(f"""{your_name} successfully {order_options[answer]}.\n
   #@@@&                                                           
  &@@@@@%\%                    -                       ,#@@..     #@        -          
 ,&&@@@@@@'        ^                         -        #@@@&@%\%   @&@%                 
   `|||'         -                    n               &@@@@@%\%   '@@"           -         
 -  |||    ^                       ^  ||               `|||'   ^   ||       -             
    /|\                    -        ./||\,              /|\           ^   
_,__.~~~~~,_,.----~~~,_,.---.~~~~~..(|  |)~~~..,,,_,__.~~~~~,--.~~~~~..,,,_,_
                                    /^-^\                             
         ~~                       _-(o.o)-_                                              
                                ~  '|| ||`          ~                    ~
  ~                ~~~              "   "                                         
                                                                ~~         
         ~      ~~                              ~                            
                                                                              
~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----
                                                                             
          ^  -                              -                              -   
                """)

                answer = input (colored(0, 255, 0,"(1) Ride the rapid    (2) Hold back     (3) Kick hard     (4) Dive under\n\n: "))
                if answer != "1" and answer != "2" and answer != "3" and answer != "4":
                    clearConsole()
                    print(colored(255, 0, 0,"You must enter a valid answer (1), (2), (3) or (4)"))
                    continue
                answer = int(answer)-1

                if order_options[answer] == correct_order[2]:
                    clearConsole()
                    print(f"""{your_name} sucessfully {order_options[answer]}.\n
   #@@@&                                                           
  &@@@@@%\%                    -                       ,#@@..     #@        -          
 ,&&@@@@@@'        ^                         -        #@@@&@%\%   @&@%                 
   `|||'         -                                    &@@@@@%\%   '@@"           -         
 -  |||    ^                       ^                   `|||'   ^   ||       -             
    /|\                    -                            /|\           ^   
_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,-n.~~~~~..,,,_,__.~~~~~,--.~~~~~..,,,_,_
                                     ||                              
         ~~                        ./||\,                                              
                                ~  (|  |)           ~                    ~
  ~                ~~~             /^-^\                                          
                                 _-(o.o)-_                      ~~         
         ~      ~~                '|| ||`       ~                            
                                   "   "                                        
~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----
                                                                             
          ^  -                              -                              - 
                    """)

                    answer = input (colored(0, 255, 0,"(1) Ride the rapid    (2) Hold back     (3) Kick hard     (4) Dive under\n\n: "))
                    if answer != "1" and answer != "2" and answer != "3" and answer != "4":
                        clearConsole()
                        print(colored(255, 0, 0,"The current pulls you back, because you must enter a valid answer (1), (2), (3) or (4)"))
                        continue
                    answer = int(answer)-1

                    if order_options[answer] == correct_order[3]:
                        clearConsole()
                        print(f"""{your_name} sucessfully {order_options[answer]}.\n
   #@@@&                                                           
  &@@@@@%\%                    -                       ,#@@..     #@        -          
 ,&&@@@@@@'        ^                         -        #@@@&@%\%   @&@%                 
   `|||'         -                                    &@@@@@%\%   '@@"           -         
 -  |||    ^                       ^                   `|||'   ^   ||       -             
    /|\                    -                            /|\           ^   
_,__.~~~~~,_,.----~~~,_,.---.~~~~~..,--.~~~~~..,,,_,__.~~~~~,--.~~~~~..,,,_,_
                                                                    
         ~~                                                                         
                                ~    n             ~                    ~
  ~                ~~~              ||                                         
                                  ./||\,                       ~~         
         ~      ~~                (|  |)        ~                            
                                  /^-^\                                          
~~~,_,.---.~~~~~..,,,_,__.~~~~~,_-(o.o)-_~,_,.---.~~~~~..,,,_,__.~~~~~,_,.----
                                 '|| ||                                          
          ^  -                    "   "          -                              -   
                        """)
                        order_solved = True
                        input("You just about made it! (press enter)\n")
                        # print("Correct order was:",correct_order)

                    else:
                        clearConsole()
                        print(f"So close! But as {your_name} attempts to {order_options[answer]} the current drags the cat all the way back to shore.")
                else:
                    clearConsole()
                    print(f"{your_name} attempts to {order_options[answer]} but the current pulls the cat right back.")
            else:
                clearConsole()
                print(f"{your_name} attempts to {order_options[answer]} but the current pulls the cat right back.")
        else:
            clearConsole()
            print(f"{your_name} decides to {order_options[answer]} but as soon as {your_name} try to enter the water, the current pulls the cat right back. Try something else.")




    scents = {'flowers':random.randint(1,25),'smelly_dog':random.randint(26,50),'bbq':random.randint(51,75),'kibble':random.randint(76,100)}

    typewrite(f"""Heavy and waterlogged, the cat slumbers onto the embankment, and once there starts grooming their sad, soggy pelt.\n
'Never. Again.' {your_name} affirms.

{your_name}'s nose catches a wiff of something in the air... wait.. there's a few things {your_name} can smell. {your_name} RECOGNISES these smells from home..

Just....
        can't quite.... 
                        ....pinpoint the direction they're coming from.
    """)
    input("\n(press enter)")

    while True:
        # print(scents) #FOR TESTING ONLY
        clearConsole
        answer = input(f"\nAttune {your_name}'s scent detection... (type a number between 1 and 100): ")

        if answer.isdigit() == False or int(answer) > 100:
            print(colored(255, 0, 0,"ERROR: You must enter a valid number between 1 and 100 to continue!"))
            continue

        answer = int(answer)
        print("""
            )                ,
          (              ___//\,^.
           )          ,-`  //  \`'-,
          '         ,'     `\  ,\   `-,
           . )     /   ___             `\\
            )   _-'  <(O'/``  \          `\\
           (   |/`     `' __  /
              _ \\',`.-____   <
               / `-__,..-/_`
                    `---'-~\\
                            \\""")

        if answer == scents['flowers']:
            print(f"\n{your_name} has locked onto the flower smell!\n")
            print(colored(0, 255, 0,"(1) Follow the flower smell               (2) Continue investigating for other scents".center(180)))
            answer = input(colored(0, 255, 0,"\n                                                 : "))
            if answer == '1':
                typewrite(f"\n{your_name} follows the flower smell. It leads to a beautiful garden of honeysuckle flowers.\nThey are the same flowers that {your_name}'s owner grows. But unfortunately, this is not home.\n")
                input("(press enter)")
                input(f"\n{your_name} picks a [honeysuckle] (press enter)")
                print("""
              __/)
           .-(__(=:
        |\ |    \)
        \ ||
         \||
          \|
           |""")
                input(colored(100, 100, 255,"\n[TAKE HONEYSUCKLE]"))
                inventory.append("Honeysuckle")
                input(colored(100, 100, 255,"\n[Honeysuckle] added to inventory. (press enter)"))
                print(colored(100, 100, 255,f"Inventory: {inventory}"))
                typewrite(f"\nIt's been a long, tiring day.. and these flowers smell so good...\nInfact, so good they make {your_name} feel very relaxed so {your_name} lies down for a nap.\n\nOh.. no.. you know what that means.")
                input("\n(press enter)")
                print(f"\n{your_name} sleepwalks back to the dumpsite!")
                clearConsole
                input("\n(press enter)")
                animals.pop(0)
                animals.insert(0,"")
                animals_ind.pop(0)
                animals_ind.insert(0,"")
                answer = False
                start_game()
                return
        
        elif answer == scents['smelly_dog']:
            print(f"\n{your_name} has locked onto the smelly dog smell!\n")
            print(colored(0, 255, 0,"(1) Follow the smelly dog smell               (2) Continue investigating for other scents".center(180)))
            answer = input(colored(0, 255, 0,"\n                                                 : "))
            if answer == '1':
                typewrite(f"\n{your_name} follows the scent which leads to a familiar looking neighbourhood! ... \n\nYes! There it is! Home! ")
                input("(press enter)")
                typewrite(f"\nThat good for nothing stinky neighbours dog actually came in handy for once! \n\n{your_name} stops suddenly. Hold on.. but.. he should be in that garden over there.. chained up..... ")
                input("(press enter)")
                typewrite("\nIf he's not there...... then...... whe-- \n\n")
                input("(press enter)")
                print("""\n
                                 ,--._______,-. 
                                ,','  ,    .  ,_`-. 
                                / /  ,' , _` ``. |  )       `-.. 
                                (,';'""`/ '"`-._ ` \/ ______\\\\ 
        __________________     : ,o.-`- ,o.  )\` -'      `---.)) 
       |  GRRRhh DUD YEW  \    : , d8b ^-.   '|   `.      `    `. 
       |  JUSH CAWL        _`>  |/ __:_     `. |  ,  `       `    \ 
       \  MHEE STINKEE ?! /     | ( ,-.`-.    ;'  ;   `       :    ; 
        \______________-'      | |  ,   `.      /     ;      :    \ 
                                ;-'`:::._,`.__),'             :     ; 
                                / ,  `-   `--                  ;     | 
                                /  \                   `       ,      | 
                                (    `     :              :    ,\     | 
                                \   `.    :     :        :  ,'  \    : 
                                \    `|-- `     \ ,'    ,-'      :-.-'; 
                                :     |`--.______;     |         :    : 
                                :    /           |    |           |   \ 
                                |    ;           ;    ;          /     ; 
                               _/--' |           :`-- /          \_:_:_| 
                             ,',','  |           |___ \ 
                             `^._,--'           / , , .) 
                                                `-._,-' 
                """)
                input("(press enter)")
                answer = False
                battle('dog')
                return
        
        elif answer == scents['bbq']:
            print(f"\n{your_name} has locked onto the bbq smell!\n")
            print(colored(0, 255, 0,"(1) Follow the bbq smell               (2) Continue investigating for other scents".center(180)))
            answer = input(colored(0, 255, 0,"\n                                                 : "))
            if answer == '1':
                typewrite(f"\n{your_name} follows the bbq smell. It leads to a group of people in their garden.\n\n")
                input("(press enter)")
                typewrite(f"\n\nAlthough {your_name}'s owners do often noisily gather in this way, unfortunately, {your_name} does not recognise the houses nor the people.\n\nThis is NOT home. (press enter)\n\n")
                print(f"{your_name} retraces steps in order to try a different scent.\n")
                input("(press enter)")
                answer = False
                continue
        
        elif answer == scents['kibble']:
            print(f"\nYou've locked {your_name} onto the kibble smell!\n")
            print("colored(0, 255, 0,(1) Follow the kibble smell               (2) Continue investigating for other scents".center(180))
            answer = input(colored(0, 255, 0,"\n                                                 : "))
            if answer == '1':
                typewrite("\n\nClever choice.. it's food. Duh. Why wouldn't you follow it!")
                typewrite("\n\nGuess where it leads....\n\n")
                input("(press enter)")
                clearConsole
                game_win()
                return
        
        elif answer < scents['flowers']:
            print(f"\n{your_name} can smell a familiar flowery scent in the distance. To pinpoint it, try going higher.")

        elif answer >= scents['flowers'] and answer < scents['smelly_dog']:
            print(f"\n{your_name} can smell a familiar flowrey scent in the distance. To pinpoint it, try going lower.")
            print(f"{your_name} can smell a familiar smelly dog in the distance. To pinpoint it, try going higher.")

        elif answer >= scents['smelly_dog'] and answer < scents['bbq']:
            print(f"\n{your_name} can smell a familiar smelly dog in the distance. To pinpoint it, try going lower.")
            print(f"{your_name} can smell a bbq smell in the distance. To pinpoint it, try going higher.")

        elif answer >= scents['bbq'] and answer < scents['kibble']:
            print(f"\n{your_name} can smell a bbq in the distance. To pinpoint it, try going lower")
            print(f"{your_name} can smell your favourite kibble in the distance. To pinpoint it, try going higher.")

        
        elif answer >= scents['kibble']:
            print(f"\n{your_name} can smell your favourite kibble in the distance. Try going lower.")
            
        else:
            print(f"This one is confusing {your_name} a bit. Can't work it out. Try again.")
def A3():
    global inventory
    typewrite(f"\n{your_name} attacks the pigeon and eats him up. Delicious. That should keep {your_name} going for a while.")
    print("""

    
(:`--..___...-''``-._             |`._
  ```--...--.      . `-..__      .`/ _\  
            `\     '       ```--`.    />
            : :   :               `:`-'   <C\.___|/  
             `.:.  `.._--...___     ``--..._`,-.`,/    
                ``--..,)       ```----....__,)`-|'
    \n""")
    input(f"{your_name} caused quite a mess... (press enter)")
    print("""\n           __
          /'{>
      ____) (____
    //'--;   ;--'\\\\
   ///////\_/\\\\\\\\\\\\\\
          m m""")
    input(colored(100, 100, 255,"\n[TAKE FEATHER]"))
    inventory.append("Feather")
    input(colored(100, 100, 255,"\n[Feather] added to inventory. (press enter)"))
    print(colored(100, 100, 255,f"Inventory: {inventory}"))

    typewrite(f"\n{your_name} clambers up a fence to get a better vantage point and from there can see a broad scope of trees to the left. To the right is the sound of rushing water.\n\n")

    print(colored(0, 255, 0, "(1) Head toward the sound of water    (2) Head towards the trees ".center(150)))
    while True:
        answer = input(colored(0, 255, 0,"\n                                          : "))
        if answer == '1':
            A5()
            return
        elif answer == '2':
            A6()
            return
        else:
            print(colored(255, 0, 0,"You must select a valid option."))
            continue
def A6():
    typewrite(f"\n{your_name} enters the woods.\n")
    print("""
     ccee88oo                    # #### ####          
  C8O8O8Q8PoOb o8oo           ### \/#|### |/####                  ,@@@@@@@,
 dOB69QO8PdUOpugoO9bD        =##\/#/ \||/##/_/##/_#       ,,,.   ,@@@@@@/@@,  .oo8888o.
CgggbU8OU qOp qOdoUOdcb     =###  \/###|/ \/ # ### &&& ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
    6OuU  /p u gcoUodpP   ##_\_#\_\## | #/###_/_#### &,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
      \\\//  /douUP &&&  ## #### # \ #| /  #### ##/## %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
        \\\////     &&&/&  __#_--###`  |{,###---###-~&%&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
         |||/\   &&&\&|&/&&&         \ }{    &&&\&|&/&`&%\ ` /%&'    |.|        \ '|8'
         |||\/    &&&\|/&&&           }}{     _\&\|/&/&   |o|        | |         | |
         |||||     & }}{  &           }}{      &-}}{-&    |.|        | |         | |
   .....//||||\...-^-}{{ _, -=-~  ,  -=-~{ .-^- _}{{,~=__ \\/ ._\//-=-~_/  ,\_//__\\/.  \_....
            }                          `}                   `        ' `
                                      { 
""")
    typewrite(f"The cat wanders through the woods for what seems like hours. The sun begins to set, and it soon gets darker, and darker. With only flickers of moonlight for company, under the canopy of thick tree leaves and tangled bracken, {your_name} can barely see.")
    typewrite(f"\n\n{your_name} soon begins to hear noises.. shuffling in the undergrowth...")
    input("(Press enter)")
    print('''
              ___,,___
           _,-='=- =-  -`"--.__,,.._
        ,-;// /  - -       -   -= - "=.
      ,'///    -     -   -   =  - ==-=\`.
     |/// /  =    `. - =   == - =.=_,,._ `=/|
    ///    -   -    \  - - = ,ndDMHHMM/\\b  \\
  ,' - / /        / /\ =  - /MM(,,._`YQMM_  `|
 <_,=^Kkm / / / / ///H|wnWWdMKKK#""-;`("0\\'_;|
        `""QkmmmmmnWMMM\\""WHMKKMM\   `--. \>-\\
             `""'  `->,>,    ``WHMb,.   `-,_<@)
                                `"QMM`.     
                                   `>,>,
                                       
    ''')
    typewrite(f"""A ferocious looking badger leaps toward {your_name}. There is no time to react, before the cat is pinned violantly to the ground.
""")
    input("\n(press enter)")
    battle("badger")

#B / FOX PATH
def B1 ():
#Fox Introduction
    global inventory
    typewrite(f"Fox: Hey cat I'm Freddy The fox! I'm cunning and brave, it was a good choice to ask me to guide you home. \n\nI've grown up in this dump, spending my time building an intriquit tunnel system.")
    input ("""
                                                                  ,-,
                                                              _.-=;~ /_
                                                            _-~   '     ;.
                                                        _.-~     '   .-~-~`-._
                                                  _.--~~:.             --.____88
                                ____.........--~~~. .' .  .        _..-------~~
                      _..--~~~~               .' .'             ,'
                  _.-~                        .       .     ` ,'
                .'                                    :.    ./
              .:     ,/          `                   ::.   ,'
            .:'     ,(            ;.                ::. ,-'
            .'     ./'.`.     . . /:::._______.... _/:.o/
          /     ./'. . .)  . _.,'               `88;?88|
        ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
      _,'' . .,/',-~    d888P'                    88'  88|
  _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
  :     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
  `.;;;:='    ~~            ~~~                ~-    -       -   -
  ,---.                 ,--.   ,--.               ,--.  ,--.                 ,---.                 
  /  .-',--.--. ,---.  ,-|  | ,-|  |,--. ,--.    ,-'  '-.|  ,---.  ,---.     /  .-' ,---.,--.  ,--. 
  |  `-,|  .--'| .-. :' .-. |' .-. | \  '  /     '-.  .-'|  .-.  || .-. :    |  `-,| .-. |\  `'  /  
  |  .-'|  |   \   --.\ `-' |\ `-' |  \   '        |  |  |  | |  |\   --.    |  .-'' '-' '/  /.  \  
  `--'  `--'    `----' `---'  `---' .-'  /         `--'  `--' `--' `----'    `--'   `---''--'  '--' 
                                    `---'                                                           
  """)

    typewrite(f"Fox: Follow me {your_name}, and you'll be home by sunrise! \n\nOh and keep hold of these cherries for me. I cannot function without a snack to hand!")
    input ("(press enter)")
#Add cherries too inventory
    input("\n[TAKE CHERRIES]")
    inventory.append("cherries")
    input("\n[Cherries] added to inventory. (press enter)")
    print("Inventory: ",inventory)


    input ("""
  _____#####_____
  _____########___ 
  ______###___###### 
  _______###_____#### 
  _________####______# 
  ___________######### 
  ____________######## 
  _________________#### 
  ________________#__# 
  _______________##___## 
  ______________#_______# 
  _____________ #_________## 
  ____________ ##___________# cru
  ____________##_____________## 
  __________###__________########## 
  ____###########____##___####_### 
  ___##____#######___#__#####__#### 
  __##____##### ###__###_##_##_#### 
  __#_____#########__############# 
  __###############__########## 
  ____#############___######### 
  _____##########____ 
  """)

    typewrite("So we have two choices to get through this dump. We can either \n1- Try and get past the Robot Security Guard OR \n2- We can escape through my tunnel system.")

    escape_route = input ("  Type which option you choose 1, 2 or go back to the start:")

    if escape_route == ("1") : 
        print (f"Seems you are brave like me {your_name}. Quite unexpected for a cat I must say.")
        B4 ()
    elif escape_route == ("2"): 
        print (f" Seems you are cunning like me {your_name}. To be expected from a cat I must say. ")
        B2()
    else:                   
        print (f"You think one of those other animals could help out of this dump {your_name}?! Very unwise... but to be expected from a cat.")
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game()
def B2 ():
    input ("""
    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \.
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \.
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@%.%. @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
    """)
    #List- Fox and cat walking through dump
    typewrite(f"*Freddy and {your_name}, climbed stealthily round the mountains of trash into the Fox's tunnel system*")

    input ("""
        _..---...,""-._     ,/}/)
     .''        ,      ``..'(/-<
    /   _      {      )         \.
   ;   _ `.     `.   <         a(
 ,'   ( \  )      `.  \ __.._ .: y
(  <\_-) )'-.____...\  `._   //-'
 `. `-' /-._)))      `-._)))
   `...'         
    """)
    Where_they_climbed = [
        "Across piles of used socks",
        "Through caverns of plastic bottles",
        "Over heaps of rotting food",
        "Under mountains of rusting metal"
    ]
    input (Where_they_climbed) 

    typewrite(" *It was truly disgusting, the cat had never smelled anything so bad.*\n\
        Fox: As charming and well-built as my caves are we have come to the end of the road, only...\n\
        Now we have to try and figure out how to get through these locked gates!")
    B3()
def B3 ():
  

    #Ascii of gate
    input ("""
                        
                             !  !  ! II II !  !  !
                          !  I__I__I_II II_I__I__I  !
                          I_/|__|__|_|| ||_|__|__|\_I
                       ! /|_/|  |  | || || |  |  |\_|\ !       
           .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
          /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \,
          \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
           }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
          {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
    _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
    _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
    -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
     |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
     |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
     |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
     |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  | 
    _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
    -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
    -|--|--|| |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  | 
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~
    """)
    #Fox introduces quiz too
    typewrite (f"Fox: I believe you may be able to have climbed up these gates on a good day {your_name}, \n\
    but it's late and you look way too tired for that now! \n\
    There's this digital code thingy here.\n\
    Looks like you have to complete this maths quiz to get through")


    input (f"""
          ,-.      .-,
          |-.\ __ /.-|
          \  `    `  /
          / _     _  \.
          | _`q  p _ |
          '._=/  \=_.'   Fox: This ones on you {your_name}, I'm terrible at Maths, plus I'm slowly running out of energy here. Maybe time for some cherries soon!
            (`\()/`)`\,
            (     )  \,
            |(    )    \,
            \ '--'   .- \,
            |-      /    \,
            | | | | |     ;
            | | |.;.,..__ |
            .-"";`         `|
        /    |           /
        `-../____,..---'`
    """)

    typewrite ("Digital Gate: 'Maths quiz commencing.\n\
    These gates will either remain closed or open once your score is calculated.\n\
    Good luck!")

    flag = 1

    while flag < 5:
        print("\rLoading. Please Wait " + ("." * flag), end=" ")
        sleep(1)
        flag = flag + 1

    #Maths Quiz
    count = 0
    score_2 = 0

    while count <= 9:
        ops = (add, sub, mul)
        op = random.choice(ops)
        x = random.randint(1,10)
        y = random.randint(1,10)

        if op == add:
            print("What is", x, "+",y, "? ")
            question_add = int(input())
            answer_add = op(x,y)
            if question_add == answer_add:
                print("Well done, this is correct!")
                score_2 = score_2 + 1
                count = count + 1
            else:
                print("Sorry, but this is incorrect.")
                count = count + 1

        elif op == sub:
            print("What is", x, "-", y, "? ")
            question_sub = int(input())
            answer_sub = op(x,y)
            if question_sub == answer_sub:
                print("Well done, this is correct!")
                score_2 = score_2 + 1
                count = count + 1
            else:
                print("Sorry, but this is incorrect.")
                count = count + 1

        elif op == mul:
            print("What is", x, "x", y, "? ")
            question_mul = int(input())
            answer_mul = op(x,y)
            if question_mul == answer_mul:
                print("Well done, this is correct!")
                score_2 = score_2 + 1
                count = count + 1
            else:
                print("Sorry, but this is incorrect.")
                count = count + 1
        if count == 10:
            print("You have completed the quiz. Your final score out of 10 is "+str(score_2)+".")

    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if score_2 >= 8:
        print ("Well done! With brains like these gate will open for you.") #Link too B9
        B9 ()
    elif score_2 == 10:
        print ("Well.. it's not full marks but it's close. I guess you can go through.") #Link too B9
        B9 ()
    else:
        print ("Well you are no maths genious. I'm afraid you can't pass through the gate today.") #Link too B
        AB ()
def AB ():
    #Fox tells Cat to go to Pigeon
    typewrite (f" Fox: Well {your_name}... Maths is really not your strong suit either is it \n\
I tried my best, but I'm going to send you to my friend pigeon to guide you.")

    input ("""
                                                                    ,-,
                                                                _.-=;~ /_
                                                            _-~   '     ;.
                                                        _.-~     '   .-~-~`-._
                                                    _.--~~:.             --.____88
                                ____.........--~~~. .' .  .        _..-------~~
                        _..--~~~~               .' .'             ,'
                    _.-~                        .       .     ` ,'
                .'                                    :.    ./
                .:     ,/          `                   ::.   ,'
            .:'     ,(            ;.                ::. ,-'
            .'     ./'.`.     . . /:::._______.... _/:.o/
            /     ./'. . .)  . _.,'               `88;?88|
        ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
        _,'' . .,/',-~    d888P'                    88'  88|
    _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
    :     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
    `.;;;:='    ~~            ~~~                ~-    -       -   -

    """)
    typewrite ("Fox: just be careful, Pigeon may be worried you are going to eat him! ")

    A1()
    return
def B4 ():
    #Creeping through trash trying to avoid robot
    typewrite (f"*Freddy and {your_name}, creeped stealthily round the piles of trash, \n\
    on the look-out for the Robot security guard")

    input ("""
        _..---...,""-._     ,/}/)
     .''        ,      ``..'(/-<
    /   _      {      )         \.
   ;   _ `.     `.   <         a(
 ,'   ( \  )      `.  \ __.._ .: y
(  <\_-) )'-.____...\  `._   //-'
 `. `-' /-._)))      `-._)))
   `...'  
    """)
    #List of where they creeped
    Where_they_creeped = [
        "Across piles of used socks",
        "Through caverns of plastic bottles",
        "Over heaps of rotting food",
        "Under mountains of rusting metal"
    ]
    print (Where_they_creeped)
    # Guard finds Cat
    typewrite(f"*When suddenly beyond the lake of turned milk, the robot guard appeared.\n\
    Instantly spotting Freddy and {your_name}*")


    input ("""
                             !! Intruder spotted!!.
                           ,'
              .-----.
            ,' -   - `.
    _ _____/   
  \_____ _
   /_||   ||`-._____.-`||   ||-\.
  / _||===||           ||===|| _\.
 |- _||===||===========||===||- _|
 \___||___||___________||___||___/
  \\|///   \_:_:_:_:_:_/   \\\|//
  |   _|    |_________|    |   _|
  |   _|   /( ======= )\   |   _|
  \\||//  /\ `-.___.-' /\  \\||//
   (o )  /_ '._______.' _\  ( o)
  /__/ \ |    _|   |_   _| / \__\.
  ///\_/ |_   _|   |    _| \_/\\\.
 ///\\_\ \    _/   \    _/ /_//\\\.
 \\|//_/ ///|\\\   ///|\\\ \_\\|//
         \\\|///   \\\|///
         /-  _\\   //   _\.
         |   _||   ||-  _|
       ,/\____||   || ___/\,
      /|\___`\,|   |,/'___/|\.
      |||`.\\ \\   // //,'|||
      \\\\_//_//   \\_\\_//// 
    """)

    typewrite ("Fox: Oh no he's spotted us!!")
    #Fox introduces options of how to avoid guard
    input (f"""
          ,-.      .-,
          |-.\ __ /.-|
          \  `    `  /
          / _     _  \.
          | _`q  p _ |
          '._=/  \=_.'   Fox: Quick {your_name}, we must take action before he captures us! We could:
            (`\()/`)`\,
            (     )  \,
            |(    )    \,
            \ '--'   .- \,
            |-      /    \,
            | | | | |     ;
            | | |.;.,..__ |
         .-"";`         `|
        /    |           /
        `-../____,..---'`

    """)
    Robot_guard = [
        "1: Run straight at him and hope it gets confused",
        "2: Throw some trash into this distance and hope it gets",
        "3: Do nothing"   
    ]
    print (Robot_guard)

    Pass_Guard = input ("Which do you choose? Input 1, 2 or 3:")

    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if Pass_Guard == ("1"):
        B5 ()
    elif Pass_Guard == ("2"):
        B6 ()
    else:
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game ()
def B5 ():
    #Guard Captures Cat
    input ("""
                             !!!Intruder Captured!!!
                           ,'
              .-----.
            ,' -   - `.
    _ _____/   
  \_____ _
   /_||   ||`-._____.-`||   ||-\,
  / _||===||           ||===|| _\,
 |- _||===||===========||===||- _|
 \___||___||___________||___||___/
  \\|///   \_:_:_:_:_:_/   \\\|//
  |   _|    |_________|    |   _|
  |   _|   /( ======= )\   |   _|
  \\||//  /\ `-.___.-' /\  \\||//
   (o )  /_ '._______.' _\  ( o)
  /__/ \ |    _|   |_   _| / \__\,
  ///\_/ |_   _|   |    _| \_/\\\,
 ///\\_\ \    _/   \    _/ /_//\\\,
 \\|//_/ ///|\\\   ///|\\\ \_\\|//
         \\\|///   \\\|///
         /-  _\\   //   _\,
         |   _||   ||-  _|
       ,/\____||   || ___/\,
      /|\___`\,|   |,/'___/|\,
      |||`.\\ \\   // //,'|||
      \\\\_//_//   \\_\\_//// LGB/fsc
    """)
    typewrite ("Robot Guard: Intruder capture. Heading back to base..\n\
        All intruders will be given one chance to get free. \n\
            You must score 100 on my quiz to pass.")
    #Quiz to escapr Robot Introduced
    input (f"""
           ,-.      .-,
           |-.\ __ /.-|
           \  `    `  /
           / _     _  \.
           | _`q  p _ |
           '._=/  \=_.'   Fox: This ones on you {your_name}, I'm terrible at quizez, plus I'm slowly running out of energy here!
             (`\()/`)`\,
             (     )  \,
             |(    )    \,
             \ '--'   .- \,
             |-      /    \,
             | | | | |     ;
             | | |.;.,..__ |
          .-"";`         `|
        /    |           /
        `-../____,..---'`

    """)

    flag = 1

    while flag < 5:
        print("\rLoading. Please Wait " + ("." * flag), end=" ")
        sleep(1)
        flag = flag + 1
    # Do you want to play?
    score=0
    total_questions=3
    #Maths Quiz
    answer=input("Are you ready to play the Quiz ? (yes/no) :")
    score=0
    total_questions= 4
    
    if answer.lower()=="yes":
        answer=input("Question 1: I have 2 big ears, tusks and a trunk. What am I?")
        if answer.lower()=="elephant":
            score += 1
            print("correct")
        else:
            print("Wrong Answer :")


        answer=input("Question 2: I come in a pair and you will need to tie and untie me to get me of your feet? ")
        if answer.lower()=='shoes':
            score += 1
            print("correct")
        else:
            print("Wrong Answer :")


        answer=input("Question 3: What element does O represent in the periodic table?")
        if answer.lower()=="oxygen":
            score += 1
            print("correct")
        else:
            print("Wrong Answer :")

        answer=input("Question 4: The River that runs through Egypt is The:")
        if answer.lower()=="nile":
            score += 1
            print("correct")
        else:
            print("Wrong Answer :")
    #Score
    typewrite("You have now completed the quiz!")
    mark=(score/total_questions)*100
    typewrite(f'Marks obtained: shoes{mark}')
    
    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if score == 100:
        print (" Well done. You are free to leave") 
        B7 ()
    else:
        print ("You did not score high enough. You will be taken to the pet shelter in the Morning.")
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game ()
def B6 ():
    #Guard distracted by thrown trash
    input ("""
                             !!!Intruder detected in distant rubbish pile!!!
                           ,'
              .-----.
            ,' -   - `.
    _ _____/   
  \_____ _
   /_||   ||`-._____.-`||   ||-\.
  / _||===||           ||===|| _\.
 |- _||===||===========||===||- _|
 \___||___||___________||___||___/
  \\|///   \_:_:_:_:_:_/   \\\|//
  |   _|    |_________|    |   _|
  |   _|   /( ======= )\   |   _|
  \\||//  /\ `-.___.-' /\  \\||//
   (o )  /_ '._______.' _\  ( o)
  /__/ \ |    _|   |_   _| / \__\.
  ///\_/ |_   _|   |    _| \_/\\\.
 ///\\_\ \    _/   \    _/ /_//\\\.
 \\|//_/ ///|\\\   ///|\\\ \_\\|//
         \\\|///   \\\|///
         /-  _\\   //   _\.
         |   _||   ||-  _|
       ,/\____||   || ___/\,
      /|\___`\,|   |,/'___/|\.
      |||`.\\ \\   // //,'|||
      \\\\_//_//   \\_\\_//// LGB/fsc
    """)
    typewrite (f" Well that worked! Well done {your_name} you are as cunning as a fox!")

    B3()
def B7 ():
    global inventory
   #Fox asks for berry to get over gate
    typewrite(f" Fox: Amazing {your_name} well done I had no idea cats could be that clever!\n\
   Hey do you remember the berry I gave you earlier? \n\
   well we are just about to get to the gate and there's no way I can carry you over it.\n\
   You should eat it to get some energy!")
    input ("""
   _____#####_____
   _____########___ 
   ______###___###### 
   _______###_____#### 
   _________####______# 
   ___________######### 
   ____________######## 
   _________________#### 
   ________________#__# 
   _______________##___## 
   ______________#_______# 
   _____________ #_________## 
   ____________ ##___________# 
   ____________##_____________## 
   __________###__________########## 
   ____###########____##___####_### 
   ___##____#######___#__#####__#### 
   __##____##### ###__###_##_##_#### 
   __#_____#########__############# 
   __###############__########## 
   ____#############___######### 
   _____##########____ 
   """)

    input("[EAT BERRY]")
    inventory.remove("berry")

   #Fox asks if cat could get them over gate
    input ("""
                        
                           !  !  ! II II !  !  !
                        !  I__I__I_II II_I__I__I  !
                        I_/|__|__|_|| ||_|__|__|\_I
                     ! /|_/|  |  | || || |  |  |\_|\ !       
          .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
         /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \,
         \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
          }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
         {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
   _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
   _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
   -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
    |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
    |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
    |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
    |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  | 
   _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
   -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
   -|--|--|| |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  | 
   ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~
   """)
    typewrite ("Do you think you could carry us both over it? Those cherries are potent and should give you enough energy!")

   #IF ELSE THAT LINKS TOO OTHER LEVELS
    yes_no_2 = input ("Do you think you could carry us, type yes/no:")

    if yes_no_2 .lower == ("yes"):
        print (f" Nice one {your_name}! You should be home in no time.") 
        B8 ()
    else: 
        print ("Well I guess you better get settled in here because I can't help you past this point")
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game ()
def B8 ():
    #Cat and fox made it over fence
    input ("""
            *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                MMMM88&&&&&&&
    *           MMM88&&&&&&&&
                MMM88&&&&&&&&
                'MMM88&&&&&&'
                  'MMM8&&&'      *    
          |\___/|     /\___/\.
          )     (     )    ~( .              '
         =\     /=   =\~    /=
           )===(       ) ~ (
          /     \     /     \.
          |     |     ) ~   (
         /       \   /     ~ \ 
         \       /   \~     ~/
  ---_/\_/\__  _/_/\_/\__~__/_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  """)

    typewrite ("fox: Ooh what a lot of work that was. \n\
  Lets just rest a moment and take in the view!")

    B9()
def B9 ():
    #Fox says goodbye
    typewrite (f" Fox: Bet you are glad to be out of that dump {your_name}.\n\
    But what can I say, it's my home I'm used to my smelly trash heap.\n\
    Maybe one day I can settle down in a nice home like you!")

    input (f"""
          ,-.      .-,
          |-.\ __ /.-|
          \  `    `  /
          / _     _  \.
          | _`q  p _ |
          '._=/  \=_.'   Fox: It's been a real pleasure guiding you round {your_name}
            (`\()/`)`\,
            (     )  \,
            |(    )    \,
            \ '--'   .- \,
            |-      /    \,
            | | | | |     ;
            | | |.;.,..__ |
          .-"";`         `|
        /    |           /
        `-../____,..---'`

    """)
    typewrite ("But I'm afraid it's the end of the road for you and me.\n\
    As I have no idea how to find my way through this city, I rarely leave the dump!")

    input ("""
                       .|        ,       +
             *         | |      ((             *
                       |'|       `    ._____
         +     ___    |  |   *        |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
---~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    #Fox asks if cat wants to take night bus or go back to start
    typewrite ("You can either 1- Take the Night bus \n\
        OR 2- get help from another animal\n\
            Which will it be?")

    end_of_fox = input ("Type which option you choose 1, 2 or go back to the starts:")

    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if end_of_fox == ("1") : 
        print (f" Been nice knowing you, {your_name}. Have a safe journey")
        B10 ()

    else:                   
        print (f" Been nice knowing you, {your_name}. Have a safe journey")
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game ()
def B10 ():
    #Cat waiting at bus stop
    input (""" 
        ______
      .'      '.
      |   BUS  |
      |  STOP  |
        '.__.'
          ||
          ||
          ||       
        \\||///
    ^^^^^^^^^^^^^^^  
          
       |\      _,,,---,,_
  ZZZzz/,`.-'`'    -.  ;-' ;;,_
      |,4-  ) )-,_. ,\ (    `'-'
      '---''(_/--'  `-'\_)   
""")
    typewrite ("the cat was waiting so long for the bus he fell asleep!")
    flag = 1

    while flag < 5:
        print("\rSurely not much longer " + ("." * flag), end=" ")
        sleep(1)
        flag = flag + 1
    #Bus arives
    print ("""
'Bus driver: It's the Last train of the night cat.'
  .-------------------------------------------------------------.
  '------..-------------..----------..----------..----------..--.|
  |       \\            ||          ||          ||          ||  ||
  |        \\           ||          ||          ||          ||  ||
  |    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||
  |    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||  
  |_.------"''----------''----------''----------''----------''--'|
  |)|      |       |       |       |    |      mga|      ||==|  |
  | |      |  _-_  |       |       |    |  .-.    |      ||==| C|
  | |  __  |.'.-.' |   _   |   _   |    |.'.-.'.  |  __  | "__=='
  '---------'|( )|'----------------------'|( )|'----------""
              '-'                          '-'
  """)

    typewrite ("*Cat is awoken by the voice of the driver. Tired and ready to go back to his cat bed*")

    yes_no_3 = input ("Busdriver: You getting on or what? type yes/no:") 


    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if yes_no_3.lower == ("yes"):
        print ("Hop on then Cat, no need for a ticket pets ride free!")
        game_win()
    else: 
        print ("Then you are stranded here cat.") #link too start
        animals.pop(1)
        animals.insert(1,"")
        animals_ind.pop(1)
        animals_ind.insert(1,"")
        start_game ()

#C / RAT PATH
def C1():
    typewrite("Hi, I am Ratty, the landfill upcyling genius")  
    input ("""
  .--,       .--,
 ( (  \.---./  ) )
  '.__/o   o\__.'
     {=  ^  =}
      >  -  <
     /       \'
    //       \\
   //|   .   |\\
   "'\       /'"_.-~^`'-.
      \  _  /--'         `
    ___)( )(___
   (((__) (__)))
 """)
    typewrite("I hear you are in a spot of bother? I think I can help you \n\
    I have upcycled a car and a plane from junk'n'rubbish from around the landfill, I can hopefully take you home")

    input ("""
                              _.-=._-         _
                         _.-=.   _-          | ||.......---._______     __..
             ___.===....-.______-,,,,,,,,,,,,`-..----. ....       .....  __'
      __.--..     __        ,'                   o \           __        [__|
  __-..=======.--..  ..--.=================================.--..  ..--.=======:
 ]       [w] : /        \ : |========================|    : /        \ :  [w] :
 V___________:|          |: |========================|    :|          |:   _-.
 V__________: \        / :_|=======================/_____: \        / :__-.
 -----------'  .-____-.  .-------------------------------'  .-____-.
 """) 
    input ("""
            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
 """)
    typewrite("Ratty asks. Which vehicle would you like")
    answer = input("Car(1) Plane(2)?")
    if answer == '1':
        typewrite("Car")
        C2()
    elif answer == '2':
        typewrite("Plane")
        C3()
def C2():
    typewrite("Which way do you wanna go")
    answer = typewrite("Scenic route(1) Through the city(2)?")
    if answer == '1':
        typewrite("scenic route")
        C4()
    elif answer == '2':
        typewrite("Through the city")
        C5()
def C3():
    typewrite("There is a Tornado right ahead. Do you:")
    answer = input("Stay(1) or Jump(2)?")
    if answer == '1':
        typewrite("Stay")
        C6()
    elif answer == '2':
        print("Jump")
        C7()
def C4():
    typewrite("Something Spooky")
    input ("""
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\.
 .  :    .     . _ :::/:               .  ^ .  . .:\.
  .. . .   . - : :.:./.                        .  .:\.
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\.
""")
    answer = input("Alien(1) Haunted house(2)?")
    if answer == '1':
        typewrite("Alien")
        C8()
    elif answer == '2':
        typewrite("Haunted house")
        C9()
def C5():
    typewrite("A few minutes into the journey. Disaster happens. You can either:")
    answer = input("Break down(1) Crash into lampost(2)?")
    if answer == '1':
        typewrite("Break down")
        C10()
    elif answer == '2':
        typewrite("Crash into lampost")
        C11()
def C6():
    typewrite("As the plane flies into the tornado. There is a massive thud. Cat is now in a magical land, and is approached by a:")
    input ("""
                 .##@@&&&@@##.
              ,##@&::%&&..::&@##.
             #@&:..000000000..:&@#
           #@&:%00'         '00%:&@#
          #@&:%0'             '0%:&@#
         #@&:%0                 ..:&@#
        #@&:%0                   ..:&@#
        #@&:%0                   ..:&@#
        .. ...                   ......
      _oOoOoOo_                  ...... 
     (oOoOoOoOo)                 ......
      )`.....`(                    ...
     /         \                    .
    | #         |                   .
    \           /                   .
     `=========`                    . 
                                   _ |\_
                                   \` ..\.
                              __,.-" =__Y=
                            ."        )
                      _    /   ,    \/\_
                     ((____|    )_-\ \_-`
                     `-----'`-----` `--`
 """)
    input ("""
.✫*ﾟ･ﾟ｡.☆.*｡･ﾟ✫*.
.✫*ﾟ･ﾟ｡.★.*｡･ﾟ✫*.
.・。.・゜✭・.・✫・゜・。.
*✭˚･ﾟ✧*･ﾟ*✭˚･ﾟ✧*･ﾟ*
`*:;,．★ ⌒ ☆・:.,;*
.･:*:･ﾟ’✫,’✫’ﾟ･:*:･                        _
                       | \;
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆☆ ⌒ ★
""")
# Mouse 1
    answer = input("Magic cat(1) Rainbow cat(2)?")
    if answer == '1':
        typewrite("Magic cat")
        C12()
    elif answer == '2':
        typewrite("Rainbow cat")
        C13()
def C7():
    typewrite("Very brave. What now?")
    answer = input("Fall onto a stray helium balloon(1) Saved by ratty with a back-pack super rocket?(2)?")
    if answer == '1':
        typewrite("Balloon")
        C14()
    elif answer == '2':
        typewrite("Ratty")
        C15()
def C8():
    typewrite("The alien is waving at you on the roadside. He needs your help")
    input ("""
      .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
     __||__//
    /.    _/
   // \  /
  //   ||
  \\  /  \.
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
 """)
    
    answer = input("Dont help(1) Help(2)?")
    if answer == '1':
        typewrite("Don't help")
        C16()
    elif answer == '2':
        typewrite("Help")
        C17()
def C9():
    typewrite("The ghost in the house needs help")
    input ("""

                ,
                 \`-,      ,     =-
             .-._/   \_____)\.
            ("              / =-
             '-;   ,_____.-'       =-
              /__.'

 """)
    answer = input("Don't help(1) Help(2)?")
    if answer == '1':
        typewrite("don't help")
        C18()
    elif answer == '2':
        typewrite("help")
        C19()
def C10():
    typewrite("Cat recognises where he is. What does he have?:")
    answer = input("Day dream(1) Nightmare/Afternoonmare(2)?")
    if answer == '1':
        typewrite("day dream")
        C20()
    elif answer == '2':
        typewrite("Nightmare/Afternoonmare")
        C21()
def C11():
    typewrite("Ouch!!! After a bump on the head. cat remembers where he is")
    answer = input("day dream(1) nightmare(2)?")
    if answer == '1':
        typewrite("day dream")
        C22()
    elif answer == '2':
        typewrite("nightmare")
        C23()
def C12():
    typewrite("The Magic cat explains that he can help cat return home. But, it is risky. Never has this spell been used before")
    input ("""
 .✫*ﾟ･ﾟ｡.☆.*｡･ﾟ✫*.
 .✫*ﾟ･ﾟ｡.★.*｡･ﾟ✫*.
 .・。.・゜✭・.・✫・゜・。.
  *✭˚･ﾟ✧*･ﾟ*✭˚･ﾟ✧*･ﾟ*
 `*:;,．★ ⌒ ☆・:.,;*
  .･:*:･ﾟ’✫,’✫’ﾟ･:*:･    _
                       | \;
                       | |
                       | |
    |\                 | |
  /, ~\                / /
 X     `-.....-------./ /
  ~-. ~  ~              |
     \             /    |
      \  /_     ___\   /
      | /\ ~~~~~   \ |
      | | \        || |
      | |\ \       || )
     (_/ (_/      ((_/
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆☆ ⌒ ★
 """)
    answer = input("Trust(1) Don't trust(2)?")
    if answer == '1':
        typewrite("receive gift'n'start again")
        C24()
    elif answer == '2':
        typewrite("parallel universe")
        C4()
def C13():
    typewrite("rainbow cat request")
    input ("""
 .✫*ﾟ･ﾟ｡.☆.*｡･ﾟ✫*.
 .✫*ﾟ･ﾟ｡.★.*｡･ﾟ✫*.
 .・。.・゜✭・.・✫・゜・。.
  *✭˚･ﾟ✧*･ﾟ*✭˚･ﾟ✧*･ﾟ*
 `*:;,．★ ⌒ ☆・:.,;*
  .･:*:･ﾟ’✫,’✫’ﾟ･:*:･    _
                       | \;
                       | |
                       | |
    |\                 | |
  /, ~\                / /
 X     `-.....-------./ /
  ~-. ~  ~              |
     \             /    |
      \  /_     ___\   /
      | /\ ~~~~~   \ |
      | | \        || |
      | |\ \       || )
     (_/ (_/      ((_/
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆
    ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆ ⌒ ★ ⌒ ☆☆ ⌒ ★
 """)
    answer = input("rub paws(1) swish tail(2)?")
    if answer == '1':
        typewrite("rub paws")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
    elif answer == '2':
        typewrite("swish tail")
        C1()
def C14():
    typewrite("get sucked into the tornado")
    answer = input("magically spins back home(1) spins back to the start(2)?")
    if answer == '1':
        typewrite("magically spins back home")
        game_win()
    elif answer == '2':
        print("spins back to the start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C15():
    typewrite("Rat saves cat. But, there is a malfuction. Where do they end up?")
    answer = input("Circus(1) Fair (2)?")
    if answer == '1':
        print("Circus")
        C80()
    elif answer == '2':
        print("Fair")
        C81()
def C16():
    typewrite("You are not going to help me? ok, I am transporting you back to the:")
    answer = input("Start(1) Start(2)?")
    if answer == '1':
        print("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
    elif answer == '2':
        print("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C17():
    typewrite("Thank you for helping. I was testing your kindness, and you have passed. Now here's your reward")
    answer = input("Home (1) Start game again(2)?")
    if answer == '1':
        typewrite("Home")
        game_win()
    elif answer == '2':
        typewrite("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
def C18():
    typewrite("Thanks for nothing. Get out of my house")
    answer = input("Start (1) Start(2)?")
    if answer == '1':
        print("Start")
        start_game ()
    elif answer == '2':
        typewrite("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C19():
    typewrite("Thank you for helping me. I just wanted to find out if you were helpful and kind. I will now reward you with:")
    answer = input("Home(1) Start(2)?")
    if answer == '1':
        typewrite("Home")
        game_win()
    elif answer == '2':
        typewrite("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C22():
    typewrite("You have been through a traumatic experience. Get away from this situation")
    answer = input("Start again 1 (1) Ratty start 2(2)?")
    if answer == '1':
        print("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
    elif answer == '2':
        print("Ratty start")
        C1()
def C23():
    typewrite("Cat remembers where he is. The vet surgery is in front of him. It scares me. I want to start again or anyone but here")
    answer = input("Start again(1) Ratty start(2)?")
    if answer == '1':
        print("start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
    elif answer == '2':
        print("Ratty start")
        C1()
def C24():
    typewrite("The spell has gone wrong. Instead of home, cat is now caught up into a parallel universe")
    answer = input("Start again(1) Enter parallel universe(2)?")
    if answer == '1':
        typewrite("Start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
    elif answer == '2':
        typewrite("parallel universe")
        C4()
def C80():
    input("Cat'n'rat fall into a circus. They meet a:")
    input ("""
   _
  ( \                ..-----..__
   \.'.        _.--'`  [   '  ' ```'-._
    `. `'-..-'' `    '  ' '   .  ;   ; `-'''-.,__/|/_
      `'-.;..-''`|'  `.  '.    ;     '  `    '   `'  `,
                 \ '   .    ' .     '   ;   .`   . ' 7 \.
                  '.' . '- . \    .`   .`  .   .\     `Y
                    '-.' .   ].  '   ,    '    /'`""';:'
                      /Y   '.] '-._ /    ' _.-'
                      \'\_   ; (`'.'.'  ."/
                       ' )` /  `.'   .-'.'
                        '\  \).'  .-'--"
                          `. `,_'`
                            `.__)  
""")
    input ("""
                __,__
             .--.  .-"     "-.  .--.
            / .. \/  .-. .-.  \/ .. \.
           | |  '|  /   Y   \  |'  | |
           | \   \  \ 0 | 0 /  /   / |
            \ '- ,\.-"`` ``"-./, -' /
             `'-' /_   ^ ^   _\ '-'`
             .--'|  \._ _ _./  |'--.
           /`    \   \.-.  /   /    `\.
          /       '._/  |-' _.'       \.
         /          ;  /--~'   |       \.
        /        .'\|.-\--.     \       \.
       /   .'-. /.-.;\  |\|'~'-.|\       \.
       \       `-./`|_\_/ `     `\.'.      \.
        '.      ;     ___)        '.`;    /
          '-.,_ ;     ___)          \/   /
           \   ``'------'\       \   `  /
            '.    \       '.      |   ;/_
       ___>     '.       \_ _ _/   ,  '--.
        .'   '.   .-~~~~~-. /     |--'`~~-.  \.
       // / .---'/  .-~~-._/ / / /---..__.'  /
      ((_(_/    /  /      (_(_(_(---.__    .'
                | |     _              `~~`
                | |     \'.
                 \ '....' |
                  '.,___.'
 """)
    answer = input("Tiger(1) Monkey(2)?")
    if answer == '1':
        typewrite("Tiger")
        C90()
    elif answer == '2':
        typewrite("Monkey")
        C92()
def C81():
    typewrite("Cat'n'rat fall into a fair. They meet a")
    input ("""
                  .--,       .--,
                 ( (  \.---./  ) )
                  '.__/o   o\__.'
                     {=  ^  =}
                      >  -  <
       ___________.""`-------`"".____________
      /  o                            O      \.
      \                                      /
      /  .    O                          o   \.
      \                                      /         __
      /                                      \     _.-'  `.
      \______________o__________o____________/ .-~^        `~--'
                    ___)( )(___        `-.___.'
                   (((__) (__)))
 """)
    input ("""
       /`-._
      /_,.._`:-         
  ,.-'  ,   `-:..-')   
 : o ):';      _  {   
  `-._ `'__,.-'\`-.)
      `\\  \,.-'`
 """)
 
    answer = input("Goldfish(1) Mouse(2)?")
    if answer == '1':
        typewrite("Goldfish")
        C91()
    elif answer == '2':
        typewrite("Mouse")
        C92()
def C20():
    typewrite("Cat remembers the pet shop and the post office. Which place does he visit?")
    answer = input("Pet Shop(1) Post Office(2)?")
    if answer == '1':
        typewrite("Pet Shop")
        C600()
    elif answer == '2':
        typewrite("Post Office")
        C500()
def C500():
    typewrite("In the Post Office there is a free map and cat snacks. Which one does cat take? Beware wrong choice and you start all over again")
    answer = input("Free Map (1) Cat Snack(2)?")
    if answer == '1':
        typewrite("Free Map")
        C300()
    elif answer == '2':
        typewrite("Cat Snack")
        C400()
def C300():
    typewrite("The map shows cat exactly where home is. Does he:")
    answer = input("Return home (1) Start again (2)?")
    if answer == '1':
        typewrite("Return home")
        game_win()
    elif answer == '2':
        typewrite("Start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C400():
    typewrite("Cat snacks during a crisis? No way:")
    answer = input("Return home (1) Start again (2)?")
    if answer == '1':
        typewrite("Start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
    elif answer == '2':
        print("Start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C600():
    typewrite("There is a Parrot in the pet shop, sitting on a perch on the counter. Parrot asks. Can I help you? Be careful not to offend Parrot")
    input ("""
                           | \/|
   (\   _                  ) )|/|
       (/            _----. /.'.'
 .-._________..      .' @ _\  .'   
 '.._______.   '.   /    (_| .')
   '._____.  /   '-/      | _.' 
    '.______ (         ) ) \'
      '..____ '._       )  )
         .' __.--\  , ,  // ((
         '.'  mrf|  \/   (_.'(  
                 '   \ .' 
                  \   (
                   \   '.
                    \ \ '.)
                     '-'-'
 """)
    answer = input("Yes(1) NO(2)?")
    if answer == '1':
        typewrite("Yes")
        C620()
    elif answer == '2':
        typewrite("No")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
def C620():
    typewrite("Before I help you, what do you think of these jokes? Why did the cat ask for a drum set? To make mewsic")
    typewrite("What's a cat's favourite cereal? Mice Crispies")
    typewrite("what does a cat say after making a joke? Just kitten")
    typewrite("What do you think of my jokes. Bad? Awful? I'm offended. Start from the beginning")
    answer = input("Bad(1) Awful(2)?")
    if answer == '1':
        typewrite("Yes")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
    elif answer == '2':
        typewrite("No")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game ()
def C21():
    typewrite("Cat recognises the cat's home in front of him. Where he stayed as a kitten. Cat's sad, and wants to go back too:")
    answer = input("The Start(1) Back to Ratty start(2)?")
    if answer == '1':
        typewrite("Start")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
    elif answer == '2':
        typewrite("Ratty start")
        C1()
def C90():
    typewrite("I'm gonnna tell you a joke, says Tiger. I'm surrounded by pickled vegetables in jars. It's like Piccalili Circus here.")
    answer = input("Laugh(1) Awful Joke(2)?")
    if answer == '1':
        typewrite("Laugh")
        game_win()
    elif answer == '2':
        typewrite("Awful Joke")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C91():
    typewrite("I'm gonnna tell you a joke. What fish do goldfish see when they need an operation? A sturgeon")
    answer = input("Laugh(1) Awful Joke(2)?")
    if answer == '1':
        typewrite("Laugh")
        game_win()
    elif answer == '2':
        typewrite("Awful Joke")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C92():
    typewrite("I'm gonnna tell you a joke. Which mouse was a Roman leader and emperor? Julius Cheeser.")
    answer = input("Laugh(1) Awful Joke(2)?")
    if answer == '1':
        typewrite("Laugh")
        game_win()
    elif answer == '2':
        typewrite("Awful Joke")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()
def C100():
    typewrite("hey, you now have a choice. ")
    answer = input("start again (1) go home(2)?")
    if answer == '1':
        typewrite("go home")
        game_win()
    elif answer == '2':
        print("start again")
        animals.pop(2)
        animals.insert(2,"")
        animals_ind.pop(2)
        animals_ind.insert(2,"")
        start_game()

#TO DO: CONTINUOUS DEBUG
#REFORMATTING / NEATENING UP

#COLOUR REFERENCE
# print(colored(255, 0, 0, 'RED'))
# print(colored(0, 255, 0, 'GREEN'))
# print(colored(100, 100, 255, 'BLUE'))

intro()