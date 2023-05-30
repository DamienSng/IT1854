height = int(input(f'input the height of the diamond'))

spaces1 = (height // 2)
cp = spaces1 + 1
spaces2 = 1
o=0
a = '*'
s = ' '
for x in range(height + 1):

    if x < cp:

        print(f'{s * (spaces1+1)}', end='')
        print(f'{a * (x * 2 - 1)} ', end='\n')      #need to decrease spaces as x incerases
        spaces1 -= 1


    elif x == cp:
        print(f'{a * (x * 2 - 1)} ', end='\n')
        o=(x * 2 - 1)

    elif x > cp:
        print(f'{s*spaces2}', end='')
        o-=2
        print(f'{a * o}', end='\n')

        #print(f'{a * (x * 2 - 1)} ', end='\n')
        spaces2 += 1
