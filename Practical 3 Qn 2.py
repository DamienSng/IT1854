while True:
    Price = float(input('enter price of the item before tax $'))
    Quantity = float(input('enter number of items '))
    ST = Price * Quantity
    Tax = ST/100 * 7
    Total = Tax + ST
    print(f'your total is ${Total} after 7% tax')