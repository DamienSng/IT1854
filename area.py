import math
print('enter 1 for circle area')
print('enter 2 for triangle area')
print('enter 3 for square area')
print('enter 4 for rectangle area')
m=int(input())
if m==1:
    radius = int(input("enter radius"))
    print(math.pi*radius**2)
if m==2:
    length = int(input("enter length"))
    breath = int(input("enter breath"))
    print(0.5*length*breath)
if m==3:
    length = int(input("enter length"))
    print(length**2)
if m==4:
    length = int(input("enter length"))
    breath = int(input("enter breath"))
    print(length*breath)
