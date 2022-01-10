import random

#let's play a game together

game_string = ("rock","paper","scissors")

computer_choice = random.choice(game_string)


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(user_choice >= 3):
    print("Your input is invalid!!! Please input 0, 1 or 2")
    exit()
print(f"User Chose:  {game_string[user_choice]}")
print(f"Computer chose:  {computer_choice}")

if(user_choice == 0):
    if(computer_choice == "scissors"):
        print("You Win! Rock beats Scissors")
    elif(computer_choice == "paper"):
        print("You Loose:( Paper beats rock")
    else:
        print("It's a Draw")
elif(user_choice == 1):
    if(computer_choice == "scissors"):
        print("You Loose:() Scissors beats Paper")
    elif(computer_choice == "rock"):
        print("You Win!( Paper beats rock")
    else:
        print("It's a Draw")
elif(user_choice == 2):
    if(computer_choice == "paper"):
        print("You Scissors! Rock beats Paper")
    elif(computer_choice == "rock"):
        print("You Loose:( Rock beats Scissors")
    else:
        print("It's a Draw")
