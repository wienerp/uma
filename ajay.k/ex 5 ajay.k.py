#5 python program to find the factprial of a number using recurion
# fact_recut.py
def fact(m):
    if m<=1:
        return 1
    else:
        return m*fact(m-1)
    # main program
n= int(input("enter the value of n:"))
f= fact(n)
print("the factorial of",n," is",f)
    
