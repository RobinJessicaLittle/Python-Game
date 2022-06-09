#####Fox levels ######


#Variables
fox_name = ("Freddy")
your_name = ("Place Holder name")
inventory = []

#Imports
import sys
from time import sleep
#Define
def typewriter (words):
  for char in words:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

   

def B1 () : #CHECK IF INVENTORY WORKS
#Fox Introduction

  typewriter (f"Fox: Hey cat I'm {fox_name} The fox! I'm cunning and brave, it was a good choice to ask me to guide you home. \n\
    I've grown up in this dump, spending my time building an intriquit tunnel system.")

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

  typewriter (f"Fox: Follow me {your_name}, and you'll be home by sunrise! \n\
  Oh and keep hold of these cherries for me. I cannot function without a snack to hand!")
  #Does this work?
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
#input("\n[Cherry]")
#inventory.append("Cherries")
#input("\n[Cherry] added to inventory. (press enter)")
 #print("Inventory: ",inventory)

 
  typewriter ("So we have two choices to get through this dump. We can either \n\
  1- Try and get past the Robot Security Guard OR \n\
  2- We can escape through my tunnel system.")


  escape_route = input ("  Type which option you choose 1, 2 or go back to the starts:")

  if escape_route == ("1") : 
      print (f"Seems you are brave like me {your_name}. Quite unexpected for a cat I must say.")
      B4 ()
  elif escape_route == ("2"): 
      print (f" Seems you are cunning like me {your_name}. To be expected from a cat I must say. ")
      B2()
  else:                   
      print (f"You think one of those other animals could help out of this dump {your_name}?! Very unwise... but to be expected from a cat.")
      start_game ()

def B2 () :
    #Ascii of dump
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
    typewriter (f"*{fox_name} and {your_name}, climbed stealthily round the mountains of trash into the Fox's tunnel system*")

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

    typewriter(" *It was truly disgusting, the cat had never smelled anything so bad.*\n\
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
    typewriter (f"Fox: I believe you may be able to have climbed up these gates on a good day {your_name}, \n\
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

    typewriter ("Digital Gate: 'Maths quiz commencing.\n\
    These gates will either remain closed or open once your score is calculated.\n\
    Good luck!")

    #Quiz Loading
    import time

    flag = 1

    while flag < 5:
        print("\rLoading. Please Wait " + ("." * flag), end=" ")
        time.sleep(1)
        flag = flag + 1


    #Maths Quiz
    input 
    import random
    from operator import add, sub, mul
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

def AB () :

    #Fox tells Cat to go to Pigeon

    typewriter (" Fox: Well {your_name}... Maths is really not your strong suit either is it \n\
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
    typewriter ("Fox: just be careful, Pigeon may be worried you are going to eat him! ")

    A1()

def B4 ():
    #Creeping through trash trying to avoid robot
    typewriter (f"*{fox_name} and {your_name}, creeped stealthily round the piles of trash, \n\
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
    typewriter(f"*When suddenly beyond the lake of turned milk, the robot guard appeared.\n\
    Instantly spotting {fox_name} and {your_name}*")


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

    typewriter ("Fox: Oh no he's spotted us!!")
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
    typewriter ("Robot Guard: Intruder capture. Heading back to base..\n\
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


    #Quiz Loading
    import time

    flag = 1

    while flag < 5:
        print("\rLoading. Please Wait " + ("." * flag), end=" ")
        time.sleep(1)
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
    typewriter("You have now completed the quiz!")
    mark=(score/total_questions)*100
    typewriter(f'Marks obtained: shoes{mark}')

    
    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if score == 100:
        print (" Well done. You are free to leave") 
       
    else:
        print ("You did not score high enough. You will be taken to the pet shelter in the Morning.")
        

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
    typewriter (f" Well that worked! Well done {your_name} you are as cunning as a fox!")

    B3()

def B7 (): #CAN YOU REMOVE FROM INVENTORY

   #Fox asks for berry to get over gate
   typewriter (f" Fox: Amazing {your_name} well done I had no idea cats could be that clever!\n\
   Hey do you remember the berry I gave you earlier? \n\
   well we are just about to get to the gate and there's no way I can carry you over it.\n\
   You should eat it to get some energy!")
   #BERRY FROM INVENTORY FIGURE OUT CODE FOR THIS
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
   typewriter ("Do you think you could carry us both over it? Those cherries are potent and should give you enough energy!")

   #IF ELSE THAT LINKS TOO OTHER LEVELS
   yes_no_2 = input ("Do you think you could carry us, type yes/no:")

   if yes_no_2 .lower == ("yes"):
      print (f" Nice one {your_name}! You should be home in no time.") 
      B8 ()
   else: 
      print ("Well I guess you better get settled in here because I can't help you past this point")
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

  typewriter ("fox: Ooh what a lot of work that was. \n\
  Lets just rest a moment and take in the view!")

  B9()

def B9 ():

    #Fox says goodbye
    typewriter (f" Fox: Bet you are glad to be out of that dump {your_name}.\n\
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
    typewriter ("But I'm afraid it's the end of the road for you and me.\n\
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
    typewriter  ("You can either 1- Take the Night bus \n\
        OR 2- get help from another animal\n\
            Which will it be?")

    end_of_fox = input ("Type which option you choose 1, 2 or go back to the starts:")

    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if end_of_fox == ("1") : 
        print (f" Been nice knowing you, {your_name}. Have a safe journey")
        B10 ()

    else:                   
        print (f" Been nice knowing you, {your_name}. Have a safe journey")
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
  typewriter ("the cat was waiting so long for the bus he fell asleep!")
  #Loading animation
  from curses import beep
  import time

  flag = 1

  while flag < 5:
      print("\rSurely not much longer " + ("." * flag), end=" ")
      time.sleep(1)
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

  typewriter  ("*Cat is awoken by the voice of the driver. Tired and ready to go back to his cat bed*")

  yes_no_3 = input ("Busdriver: You getting on or what? type yes/no:") 


  #IF ELSE THAT LINKS TOO OTHER LEVELS
  if yes_no_3 .lower == ("yes"):
    print ("Hop on then Cat, no need for a ticket pets ride free!")
    game_win()
  else: 
    print ("Then you are stranded here cat.") #link too start
    start_game ()

B1 () 