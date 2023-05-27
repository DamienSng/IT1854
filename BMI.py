weight = float(input('enter your weight in kg '))
height = float(input('enter your height in m '))

BMI = weight/(height**2)

if BMI<18.5:
    SBMI='Underweight'

elif BMI<23 and BMI>=18.5:
    SBMI='Normal'

elif BMI<27.5 and BMI>=23:
    SBMI='Overweight'

else:
    SBMI='Obese'

BMI= BMI.__round__(2)
print(f'your BMI is {BMI} and you are {SBMI}')