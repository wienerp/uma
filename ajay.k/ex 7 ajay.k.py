str=input("enter the string:")
uppercase=0
lowercase=0
for i in str:
    if(i.isupper()):
      uppercase+=1
    elif(i.islower()):
      lowercase+=1
    print("the number of uppercase character is:")
    print(uppercase)
    print("the number of lowercase character is:")
    print(lowercase)
