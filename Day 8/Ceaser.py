letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
d=len(letters)
# txt=input("tYPE Encode to encrypt or Decode to Decrypt").lower()
txt=input("enter text? :").lower()
shift=int(input("Enter shift key ? :"))

def encrypt(plain_txt,sift_amt):
    new_txt=""
    for let in plain_txt:
        position=letters.index(let)
        new_pos=position+shift
        new_lett=letters[new_pos]
        new_txt=new_txt+new_lett
    print(new_txt)

encrypt(txt,shift)