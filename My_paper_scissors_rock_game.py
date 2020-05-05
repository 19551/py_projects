#for computer's choice we need random library
import random

#print rules of the game for user

print("Hello! Let's play Rock, scissors, paper. These are rules: \n"
                                      + "Rock beats scissors \n  "
                                      + "Paper beats rock \n  "
                                      + "Scissors beats paper\n  "
                                      + "Good luck!")


while True:
    
    print("\n"
          +"Enter your choice: \n"
          +"1 for rock\n"
          +"2 for paper\n"
          +"3 for scissors")
    #we take user choice from input
    choice=int(input("Your choice:"))
    #in case user write wrong number
    while choice>3 and choice<1:
        choice=int(input("Enter valid choice"))

    #put name for user's choice
    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    else:
        choice_name="Scissors"

    print("User's choice is " + choice_name)
    print("And computer's choice is ...")

    #generate random computer number
    comp_choice = random.randint(1,3)
    #to avoid same numbers
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3)
    #put name for computer choice
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissors"
        
    print("computer_choice is "+ comp_choice_name)
    print()
    #checking for who wins
    if ((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
        print("Paper beats")
        winner=2
    elif ((choice==1 and comp_choice==3) or (choice==3 and comp_choice==1)):
        print("Rock beats")
        winner=1
    else:
        print("Scissors beats")
        winner=3
    #checking for user or computer wins  
    if winner == choice:
        print("You are winner")
    else:
        print("Computer is winner")
    #ask if we need to continue this game and this loop
    print("Wanna play again? Enter yes or no: Y/N")
    ans=input()
    if ans=="Y" or ans=="y":
        continue
    elif ans=="N" or ans=="n":
        break

print("Thank you for playing!")


