n=int(input("how many terms?"))
F1=0
F2=1
print("the fibonacci series is")
print(F1)
print(F2)
i=3
while i<=n:
    F3=F1+F2
    print(F3)
    F1=F2
    F2=F3
    i=i+1
