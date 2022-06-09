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
    print("You have now completed the quiz!")
    mark=(score/total_questions)*100
    print(f'Marks obtained: shoes{mark}')

    
    #IF ELSE THAT LINKS TOO OTHER LEVELS
    if score == 100:
        print (" Well done. You are free to leave") 
       
    else:
        print ("You did not score high enough. You will be taken to the pet shelter in the Morning.")