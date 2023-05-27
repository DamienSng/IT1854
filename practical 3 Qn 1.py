
while True:
    try:
        cel = float(input('what is the temperature in Celsius?'))

        fer = 9 / 5 * (cel) + 32
    except:
        print(f'that is not a number')
    else:
        print(f"{cel} in celsius is {fer} in fehrenheit")