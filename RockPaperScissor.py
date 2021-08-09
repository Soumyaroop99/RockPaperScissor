# import random module
import random
comp = 0
usr = 0

# Welcome message and instructions
print("***************************WELCOME TO THE ROCK PAPER SCISSOR GAME VS COMPUTER***************************\n\n\n ")
print("RULES OF THE GAME ARE SHOWN BELOW:\n"
                                +"      ROCK VS PAPER    ----------->   PAPER WINS!!!! \n"
                                +"      ROCK VS SCISSOR  ----------->   ROCK WINS!!!! \n"
                                +"      PAPER vs SCISSOR ----------->   SCISSOR WINS!!! \n")

#Accepting user's choice and checking if its valid or not  
while True:
    print("ENTER YOUR CHOICE BELOW \n PRESS 1 FOR ROCK \n PRESS 2 FOR PAPER \n PRESS 3 FOR SCISSOR \n")
      
    # take the input from user
    choice = input("ENTER YOUR CHOICE: ")
    print('\n')
    if (choice not in ['1','2','3']):
        print("INVALID CHOICE!!! ENTER YOUR CHOICE CORRECTLY")
        quit()
    choice = int(choice)
 
          
  
    # Initialising the choice with the corresponding rock/paper/scissor
    if choice == 1:
        choice_name = 'ROCK'
    elif choice == 2:
        choice_name = 'PAPER'
    else:
        choice_name = 'SCISSOR'
          
    # print user choice 
    print("YOU HAVE CHOSEN : " + choice_name +' \n\n\n')
    print("\nNOW COMPUTER WILL CHOOSE.......")
  
    # Computer chooses randomly any number from 1-3
    comp_choice = random.randint(1, 3)
      
    # looping until comp_choice value 
    # is equal to the choice value
    while comp_choice == choice:   #not considering equal choices by both of them
        comp_choice = random.randint(1, 3)
  
    # initialize value of comp_choice_name 
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSOR'
          
    print("COMPUTER'S CHOICE IS: " + comp_choice_name)
    print('\n\n\n')
  
    print("IT IS " + choice_name + " VS " + comp_choice_name)
    print('\n')
  
    # condition for winning
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("PAPER WINS!!! \n ", end = "")
        result = "PAPER"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("ROCK WINS!!! \n", end = "")
        result = "ROCK"
    else:
        print("SCISSOR WINS \n", end = "")
        result = "SCISSOR"
  
    # Printing either user or computer wins
    if result == choice_name:
        print("********** YOU WIN!!! **********")
        usr+=1
    else:
        print("********** COMPUTER WINS!!! **********")
        comp+=1  
    print("DO YOU WANT TO PLAY AGAIN? (Y/N)")
    ans = input()
  
  
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
      
# displaying final score
print("FINAL SCORE IS")
print("YOU SCORED " + str(usr) + ' POINTS AND COMPUTER SCORED ' + str(comp) + ' POINTS \n\n' )
if (usr>comp):
    print("YOU WON!!!!")
elif (usr==comp):
    print("ITS A TIE!!! PLAY AGAIN AND DEFEAT COMPUTER!")
elif (usr<comp):
    print("YOU LOST :( TRY AGAIN AND DEFEAT COMPUTER")
print("\n********** THANKS FOR PLAYING!!! **********")