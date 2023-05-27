while True:
    num =int(input("Enter number: "))
    total = 0

    for i in range (num+1):
        i+1
        x=i%2
        if x==0:
            total = total + i
            print(f'the total is {total}')

    if num == 0:
        break
