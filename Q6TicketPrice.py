def age_check():

    age = int(input('enter your age'))

    return age

def payment(age):
    if age<16:
        print(f'you are {age} please pay $7.50')

    elif age>=16 and age<65:
        print(f'you are {age} please pay $10')

    else:
        print(f'you are {age} please pay $5.50')

def day_check():
    day = input('enter the day').lower().title().strip()
    return day

def main():
    age = age_check()
    if age>=4 and age<=130:
        day = day_check()
        if day=='Saturday' or day=='Sunday':
            print(f"it's a weekend please pay $10")
        else:
            payment(age)
    else:
        print(f'invalid age')

while True:
    main()
