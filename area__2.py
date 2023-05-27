
import math
x=int
def circle_area():
    return math.pi*radius**2
def tri_area(length,breath):
    return 0.5*length*breath
def square_area (length):
    return length**2
def rectangle_area (length,breath):
    return length*breath
print('enter 1 for circle area')
print('enter 2 for triangle area')
print('enter 3 for square area')
print('enter 4 for rectangle area')
m=int(input())
if m==1:
    radius = int(input("enter radius"))
    circle_area(radius)
if m==2:
    length = int(input("enter length"))
    breath = int(input("enter breath"))
    circle_area(radius)
    print (str(x))
if m==3:
    length = int(input("enter length"))
    circle_area(radius)
    print (str(x))
if m==4:
    length = int(input("enter length"))
    breath = int(input("enter breath"))
    circle_area(radius)
    print (str(x))
