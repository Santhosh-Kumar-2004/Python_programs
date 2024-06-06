rock ='''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
'''                                          

paper = '''


8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 
'''

scissors = '''
                     88                                                                                                             
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88         
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         
'''
import random

print("Welcome To The Rock, Paper, Scissor Game !")

#THe below code is about the user_choice.That is only consist 1,2 or 3.
user_choice = int(input("Enter 1 for 'rock' . 2 for 'paper' . 3 for 'scissors'.: \n"))
if (user_choice == 1):
    print("You Chose ROCK !")
    print(rock)
elif(user_choice == 2):
    print("You Chose PAPER !")
    print(paper)
elif(user_choice == 3):
    print("You Chose SCISSOR !")
    print(scissors)
else:
    print("Enter a Valid Choice...")

#THe below code is about the computer_choice.This prints the value of rock,paper and scissor Randomly.
computer_choice = [rock , paper , scissors]
comp_choice = random.randint(1 , 3)
if(comp_choice == 1):
    print("Computer Chose SCISSOR !")
    print(scissors)
elif(comp_choice == 2):
    print("Computer Chose ROCK !")
    print(rock)
elif(comp_choice == 3):
    print("Computer Chose PAPER !")
    print(paper)
else:
    print("Enter a Valid Choice...")

#1 .The below content is checks for only ROCK for the user_choices
if(user_choice == 1 and comp_choice == 3):
    print("YOU LOSE !!!")
elif(user_choice == 1 and comp_choice == 2):
    print("IT'S DRAW !!!")
elif(user_choice == 1 and comp_choice == 1):
    print("YOU WIN !!!")

#2 .The below content is checks for only PAPER for the user_choices
if(user_choice == 2 and comp_choice == 3):
    print("IT'S DRAW !!!")
elif(user_choice == 2 and comp_choice == 2):
    print("YOU WIN !!!")
elif(user_choice == 2 and comp_choice == 1):
    print("YOU LOSE !!!")

#3 .The below content is checks for only ROCK for the user_choices
if(user_choice == 3 and comp_choice == 3):
    print("YOU WIN !!!")
elif(user_choice == 3 and comp_choice == 2):
    print("YOU LOSE !!!")
elif(user_choice == 3 and comp_choice == 1):
    print("IT'S DRAW !!!")





