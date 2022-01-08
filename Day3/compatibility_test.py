# Take input from user
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#This is where the Magic happens
score = 0
test_string = "true"
test_string2 = "love"

#lets count 
name_combined_lower = (name1 + " "+ name2).lower()


t = name_combined_lower.count("t")
r = name_combined_lower.count("r")
u = name_combined_lower.count("u")
e = name_combined_lower.count("e")
total1 = t+r+u+e
l = name_combined_lower.count("l")
o = name_combined_lower.count("o")
v = name_combined_lower.count("v")
e = name_combined_lower.count("e")
total2 = l+o+v+e

score = int(str(total1) + str(total2))

if(score <= 10 or score >=90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
