# input from users
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


#Code where the magic happens
cheese = 1
pepperoni_s = 2
pepperoni_ml =3
pizza_s = 15
pizza_m = 20
pizza_l = 25
if(size == "S"):
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            price = pizza_s + pepperoni_s + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_s + pepperoni_s
            print(f"Your final bill is: ${price}.")
    elif(add_pepperoni == "N"):
        if(extra_cheese == "Y"):
            price = pizza_s + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_s
            print(f"Your final bill is: ${price}.")
    
elif(size == "M"):
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            price = pizza_m + pepperoni_ml + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_m + pepperoni_ml
            print(f"Your final bill is: ${price}.")
    elif(add_pepperoni == "N"):
        if(extra_cheese == "Y"):
            price = pizza_m + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_m
            print(f"Your final bill is: ${price}.")
else:
    if(add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
            price = pizza_l + pepperoni_ml + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_l + pepperoni_ml
            print(f"Your final bill is: ${price}.")
    elif(add_pepperoni == "N"):
        if(extra_cheese == "Y"):
            price = pizza_l + cheese
            print(f"Your final bill is: ${price}.")
        else:
            price = pizza_l
            print(f"Your final bill is: ${price}.")

