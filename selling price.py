while True:
    cost = float(input('enter the cost of the product'))
    increase=0
    increase=cost/100*25
    selling=cost+increase
    selling = selling.__round__(2)

    print(f'the selling prince should be ${selling}')

    if cost == 0:
        break