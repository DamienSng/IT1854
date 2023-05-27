try:
    height = float(input('enter your height in m '))

    LIW = 18.5*(height**2)
    LIW = LIW.__round__(2)

    HIW = 22.9*(height**2)
    HIW = HIW.__round__(2)

    print(f'your ideal weight range is {LIW} to {HIW}')
except:
    print(f'Invalid Input! Please try again.')