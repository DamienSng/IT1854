n=int(input('enter the length of the rectangle:'))
m=int(input('enter the width:'))
c='*'
def print_rect(n,m,c):
    for a in range(m):
        print(n*c)
print_rect(n,m,c)
input('Press enter to close')
