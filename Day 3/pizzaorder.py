print("Welcome to python")
size=input("What size pizza do you want?")
add_pepperoni=input("Do you want pepperoni")
extra_cheese=input("Do you want extmra cheese")
amount=0
if size == "S":
    amount+=15
elif size=="M":
    amount+=20

elif size=="L":
    amount==25
    if add_pepperoni=="Y":
        amount=+2
    if extra_cheese=="Y":
        amount=+1

else:
    print("Wrong Choice")
