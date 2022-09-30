import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
num_3=0
num=int(input("What do you choose? Type 0 for rock,1 for paper and 2 for Scissors"))
if num<3:
    num_3=num
else:
    print("Wrong Choice")

num_list=[rock,paper,scissors]

rand_Num=random.randint(0,2)
if num_3==rand_Num:
    print("You choose\n")
    print(num_list[num_3])
    print("\n\nComputer choose\n")
    print(num_list[rand_Num])
    print("\n\n\n\n\n You Win")
elif num_3!=rand_Num:
    print("You choose\n")
    print(num_list[num_3])
    print("\n\nComputer choose\n")
    print(num_list[rand_Num])
    print("\n\n\n\n\n You Lose")
else:
    print("Wrong Choice")
        
