str=input("enter the string:")
rev_str=" "
for i in str:
 rev_str=i+rev_str
 print("the string in reverse order:",rev_str)
if(str==rev_str):
 print("the given string is palindrome")
else:
 print("the given string is not palindrome") 
