price = float(input(f'Please enter price for item 1'))
TotalPrice = 0
i = 0
x=0
item=1

if price == 0:
    print(f'you did not buy any item.')
    print(f'Have a nice day. Looking forward to see you again')

while price != 0:
    i += 1
    TotalPrice += price
    x=1
    item+=1
    price = float(input(f'Please enter price for item {item} '))

if price == 0 and x==1:
    print(f'You have bought {i} items and the total price of ${TotalPrice}')