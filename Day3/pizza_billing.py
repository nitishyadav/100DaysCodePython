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
price = 0
if(size == "S"):
    if(add_pepperoni == "Y"):
        price = pizza_s + pepperoni_s
    else:
        price = pizza_s

    if(extra_cheese == "Y"):
        price += 1

    print(f"Your final bill is: ${price}.")

    
elif(size == "M"):
    if(add_pepperoni == "Y"):
        price = pizza_m + pepperoni_ml
    else:
        price = pizza_m 
    if(extra_cheese == "Y"):
        price += 1
    
    print(f"Your final bill is: ${price}.")
    
else:
    if(add_pepperoni == "Y"):
        price = pizza_l + pepperoni_ml
    else:
        price = pizza_l 
    if(extra_cheese == "Y"):
        price += 1
    
    print(f"Your final bill is: ${price}.")

