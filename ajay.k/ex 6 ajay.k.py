#6 python program to count the number of even and odd numbers from an array of n numbers
# even_odd_count.py
a=[ ]
even_count=0
odd_count=0
n=int(input("enter the total numbers of elements in the array:"))
for i in range(1,n+1):
 x=int(input("enter the % d element:"%i))
 a.append(x)
for i in a:
    if i %2==0:
        even_count=even_count+1
    else:
            odd_count=odd_count+1
    print("total numbers of even numbers is the array=",even_count)
    print("total numbers of odd numbers in the array=",odd_count)
