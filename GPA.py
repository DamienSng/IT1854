
while True:
    TGP = 0
    TCredit = 0
    mods=int(input('enter the amount of modules you have: '))
    for i in range (mods):
        creditP = float(input(f'enter the credits for module{i+1}: '))
        GPA=float(input(f'enter your GPA for module {i+1}: '))
        GP=GPA*creditP
        TCredit+=creditP
        TGP+=GP

    AGPA=(TGP/TCredit)
    print(f'your accumulative GPA is {AGPA}')
