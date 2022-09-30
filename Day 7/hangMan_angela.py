import random
word_list=["Hello","PLATFORM","Powershell"]
selected_word=random.choice(word_list).lower()

display=[]
for letter in selected_word:
    display+="_"
print(display)

end_of_game=False

while not end_of_game:

    guess=input("Guess A letter : ").lower()

    for position in range(len(selected_word)):
        letter=selected_word[position]
        if guess == letter:
            display[position]=letter   
    print(display)


    if "_" not in display:
        end_of_game=True
        print("You Win")
# display=[]
#
#  for chars in selected_word:
#     if guess == chars:
#         display.append(guess)
#     else:
#         display.append("_")
# print(display)