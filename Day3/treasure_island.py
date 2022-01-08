#This is where we make magic :)

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")

if(choice == "left"):
    lake = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    if(lake == "wait"):
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        if(door == "yellow"):
            print("You Win!")
        elif(door == "blue"):
            print("Eaten by beats. Game Over")
        elif(door == "red"):
            print("Burned by fire. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("You Fell into a hole. Game Over")