import random
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index+1:]

word_list=["REPLICATION"]
selected_Word=random.choice(word_list)
a=len(selected_Word)
new_word=""
while a != 0:
    da=selected_Word[a-1]
    new_word+=da.replace(da,"_")
    a-=1
# print(a)
life=len(selected_Word)
print(f"The Word is {new_word}")
new_num=0
while new_word!=selected_Word:

    user_input=input("Enter The character : ").capitalize()
    if user_input == selected_Word[selected_Word.find(user_input)]:
        print("Character Found")
        pos=[]
        numb=0
        for atPost,char in enumerate(selected_Word):
            if char == user_input:
                pos.append(atPost)
        # print(f"Character Found at place {pos}")
        while numb < len(pos):
            new_word=replacer(new_word,user_input,pos[numb])
            numb+=1
            print(new_word)
    else:
        print("Wrong Input")
        print(f"You have only life {life} left")
        if life<=0:
            print("You Lose")
            break
        life-=1
        
        
new_num+=1

if new_word==selected_Word:
    print("You Win")
    print(f"The word is {new_word}")