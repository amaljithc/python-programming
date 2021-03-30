square=lambda a:a*a
rect=lambda l,b:l*b
tria=lambda b,h:(1/2*(b*h))

print("_______area of square______")
a=int(input("enter the side="))
print("area of square=",square(a))

print("\n")
print("_______area of rectangle_______")
l=int(input("enter the length="))
b=int(input("enter the bredth="))
print("area of rectangle=",rect(l,b))

print("\n")
print("______area of triangle_______")
b=int(input("enter the bredth="))
h=int(input("enter the height="))
print("area  of traingle=",tria(b,h))