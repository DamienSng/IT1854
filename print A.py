height = int(input('Enter the height of A '))
Even = 0
Odd = 0



EoD = height % 2            #Even or Odd?
if EoD == 0:
    Even=1
elif EoD == 1:
    Odd=1


CP = (height//2)
print(f' *** ')
if Even == 1:
    SbCP = CP-1          #Star before Centre Point
    for _ in range (SbCP):
        print(f'*   *')

elif Odd == 1:
    SbCP = CP -1          #Star before Centre Point
    for _ in range (SbCP):
        print(f'*   *')

print(f'*****')

if Even == 1:
    SaCP = CP-1          #Star after Centre Point
    for _ in range (SaCP):
        print(f'*   *')

elif Odd == 1:
    SaCP = CP         #Star after Centre Point
    for _ in range (SaCP):
        print(f'*   *')




#print(f' *** ')
#print(f'*   *')
#print(f'*   *')
#print(f'*****')
#print(f'*   *')
#print(f'*   *')
#print(f'*   *')



