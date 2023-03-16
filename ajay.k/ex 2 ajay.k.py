#2. python program to calculate the total and grade of a student
#mark-list py
import os
os.system('cls')
Roll_No=int(input("enter the roll number:"))
stud_name=input("enter the student name:")
M1 =int(input("enter the mark1:"))
M2=int(input("enter the mark2:"))
M3 =int(input("enter the mark3:"))
M4 =int(input("enter the mark4:"))
M5 =int(input("enter the mark5:"))
total=M1+M2+M3+M4+M5
percentage=total/5
if percentage>=80:
    grade="A"
elif percentage>=70 and percentage<80:
    grade="B"
elif percentage>=60 and percentage<70:
    grade="C"
elif percentage>=40 and percentage<60:
    grade="D"   
else:
    grade="E"
print("roll number:",Roll_No)
print("student name:",stud_name)
print("mark1:",M1)
print("mark2:",M2)
print("mark3:",M3)
print("mark4:",M4)
print("mark5:",M5)
print("total:",total)
print("average:",percentage)
print("grade:",grade)
