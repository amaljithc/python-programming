from graphics import circle,rectangle
from graphics.Dgraphics import cuboid,sphere

r=int(input("enter the radius:"))
print("Area of cicle is:",circle.circarea(r))
print("Perimeter of circle is",circle.circperimeter(r))

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("Area of rectangle is:",rectangle.rectarea(l,b))
print("Perimeter of rectangle is:",rectangle.rectperimeter(l,b))

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
print("Area of cuboid is:",cuboid.cuboidarea(l,b,h))
print("Perimeter of cuboid is:",cuboid.cuboidperimeter(l,b,h))

r=int(input("enter the radius:"))
print("Area of sphere is:",sphere.spherearea(r))
print("Perimeter of sphere is",sphere.sphereperimeter(r))
