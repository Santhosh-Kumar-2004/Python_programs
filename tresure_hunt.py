print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')

print("Welcome To The Treasure Island !...Your Mission Is To Find The Treasure...")

user_choice1 = input("You're at a Road. Where Do You Wanna Go ? Type 'left' or 'right': ")

#First choice to the user
if (user_choice1 == "left" or user_choice1 == "Left"):
    print("You Came to a Lake. There is an Island in the middle of the Lake.")

    user_choice2 = input("Type 'wait' to wait for a Boat. Type 'swim' to Swim across or Type 'call pirates': ")

    #Second choice to the user
    if(user_choice2 == "wait" or user_choice2 == "Wait"):
        print("You Arrived at a Island Unharmed. There is a House with 3 Doors.")

        #Third choice to the user
        user_choice3 = input(" One 'Red'. One 'Yellow' . And the Finall One 'purple' Which colour would you choose? :")
        if(user_choice3 == "red" or user_choice3 == "Red"):
            print("You were Burned out With Fire !...GAME OVER.../ \n Try Again !")
        elif(user_choice3 == "purple" or user_choice3 == "Purple"):
            print("You were Eaten by the Beasts !...GAME OVER.../ \n Try Again !")
        elif(user_choice3 == "yellow" or user_choice3 == "Yellow"):

            #Fourth choice to the user
            user_choice4 = input("You've chose Corrcet door...Now an Monster standing infront of You. Type 'fight' to Fight with the Monster. Type 'hide' to Hide from the Monster.: ")
            if(user_choice4 == "fight" or user_choice4 == "Fight"):
                print("Good, You killed the Monster...!")

                #Fifth choice to the user
                user_choice5 = input("You Found Key from the Monster. Type 'Use' to use the Key on the door. Type 'keep' to keep the Key in you Bag.: ")
                if(user_choice5 == "use" or user_choice5 == "Use"):
                    print("YOU WIN !!!")
                elif(user_choice5 == "keep" or user_choice5 == "Keep"):
                    print("Safely take the Key to your Home...GAME OVER.../ \n Try Again !")

            elif(user_choice4 == "hide" or user_choice4 == "Hide"):
                print("You've found by the Monster & It ate you for Lunch...GAME OVER.../ \n Try Again !")
            else:
                print("Enter a Valid Answer...")
        else:
            print("Enter A valid Answer...")

    elif(user_choice2 == "swim" or user_choice2 == "Swim"):
        print("You were killed be the Pirahnas...GAME OVER .../ \n Try Again !")
    elif(user_choice2 == "call pirates" or user_choice2 == "Call Pirates"):
        print("The Pirates killed You and Theft Your Money and Treasure Map. GAME OVER.../ \n Try Again !")
    else:
        print("Enter A Valid Answer...")

elif(user_choice1 == "right" or user_choice1 == "Right"):
    print("You Fell into a Hole. GAME OVER.../ \n Try Again !")
else:
    print("Enter A Valid Answer...")


