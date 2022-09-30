print("Welcome to the rollercoaster!")
height = int(input("What is your height"))
if height > 120 :
    print("you Can ride roalercpaster" )
    age=int(input("What's your age"))
    if age < 12:
        print("Pls pay 7$")
    elif age > 12 & age < 18:
        print("Please pay 7")
    elif age>18:
        print("Pay 12$")
else :
    print("Sorry, you can't ride roalercpaster")
