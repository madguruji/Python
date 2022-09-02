# from cgi import print_arguments


# print("Hello world")
# print(len("hell"))

# #Data Types


# # Strings
# print("hello"[4])
# print(123_456.1+1)
# num_char = len(input("What is your name? "))
# print("Your name has "+ str(num_char) +"character")
# print(f"Your name has "+ num_char +"character")
# # print(type(num_chaalokr))

print("Welcome to the tip calculator")
bill=float(input("What is the total bill? - "))
bill_pres=float(input("What precentage tip would you like to give ? "))
split=int(input("How many people to split the bill"))
pay=bill+((bill*bill_pres)/100)
eachppl=pay/split
print(f"Each person should pay :{round(eachppl,2)}")
