TS1 = float(input('Enter your Score for Test 1:'))
TP1 = float(input('Enter your Percentage for Test 1:'))
TS2 = float(input('Enter your Score for Test 2:'))
TP2 = float(input('Enter your Percentage for Test 2:'))
TS3 = float(input('Enter your Score for Test 3:'))
TP3 = float(input('Enter your Percentage for Test 3:'))
E = float(input('Enter your Exam score:'))

FM1 = ((TS1/100)*TP1)
FM2 = ((TS2/100)*TP2)
FM3 = ((TS3/100)*TP3)
FME = ((E/100)*50)        #exam is 50%

TFM = (FM1+FM2+FM3+FME)

print('Your final mark is', TFM)
