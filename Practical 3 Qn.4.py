AI = float(input('enter you annual income '))

MI=AI/12

CPF = MI/100 * 20

MP = MI - CPF - 1500

print(f'your monthly gross income is ${MP:,}')