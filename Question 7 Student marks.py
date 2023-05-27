testmarktotal = 0
while True:
    try:
        students = int(input('How many students do you have?'))
        test = int(input('How many test for your module?'))

        for i in range (students):
            print(f'******* Student # {i+1} *******')
            for n in range (test):
                
                testmark = int(input(f'Test number {n+1}:'))
                testmarktotal = testmarktotal + testmark
            final = (testmarktotal)/test
            print(f'The average for student # {i+1} is: {final}')
            testmarktotal = 0
            final = 0
    except:
        print(f'invalid input')
