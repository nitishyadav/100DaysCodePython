
import random
# input from user
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


#Roulette code
len_names = len(names)
print(f"{names[random.randint(0,len_names-1)]} is going to buy the meal today!")
