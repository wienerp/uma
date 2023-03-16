def square(s):
 return (s*s)
def rect(l,b):
 return(l*b)
def circle(r):
 return (3.14*r*r)
def tri(b,h):
 return((b*h)/2)
a=int(input("enter side"))
b=int(input("enter breadth"))
l=int(input("enter length"))
r=float(input("enter radius"))
h=float(input("enter height"))
print("area of squ=",square(a))
print("area of circle=",circle(r))
print("area of rect=",rect(l,b))
print("area of triangle=",tri(b,h))
