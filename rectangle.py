height = int(input('enter the height of the rectangle'))
width = int(input('enter the width of the rectangle'))

rec = str('')
for _ in range (height):
    print(end='\n')
    for _ in range (width):
        rec = rec + '*'
    print(rec, end='')
    rec=('')
