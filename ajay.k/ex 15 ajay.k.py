import randome
word=[]
n=int(input("enter number of words:"))
for i in range(1,n+1):
     w=input('enter the%d word:"%i)
     words.append(w)
print("\n words in the list:")
print(words)
name=input("\what is your name?")
print("good luck!",name)
word=random.choice(word)
turns=int(input("enter the number of turns."))
print("guess the character")
guess="
while turns>0
    filed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
        if failed==0:
            print("you win")
            print("the word is:",word)
            break
            guess=input("guess the character:")
            guesses+=guess
        if guess not in word:
            turns-=1
            print("wrong")
            print("you have",+turns,'more guesses')
        if turns==0:
            print("you loose")
