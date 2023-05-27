while True:
    age=input('what is your age?')
    age=int(age)
    if(age<18):
        print('You are too young')
    if((age>=19)&(age<=25)):
        print('have you completed your NS?')
    if(age>25):
        print('open a CPF saving account!')
