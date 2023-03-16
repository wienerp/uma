print("1.faherenheit to celsius conversion")
print("2.celsius to fahrenheit conversion")
ch=int(input("enter yourn choice:"))
if ch==1:
       f=int(input("enter the temperature in fahrenheit:"))
       c=(5/9)*(f-32)
       print(f,"degree fahrenheit is equal to %.2f"%c,"degree celsius")
elif ch==2:
       c=int(input("enter the temperature in celsius:"))
       f=(9/5)*c+32
       print(c,"degree celsius is equal to %.2f"%f,"degree faherenheit")
else:
       print("wrong choice")
