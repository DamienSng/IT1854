BA = float(input('Enter the price you bought stocks for ABC Bank Corporation:'))      #BA
SA = float(input('Enter the amount of shares for ABC Bank Corporation:'))   #Stock Amount

BSB = ((SA*BA)/100)*3        #buy Stock Broker

BSB = str (BSB)
print('You have paid total commission of $'+BSB)
BSB = float (BSB)

CP = float(input('Enter the current price for ABC Bank Corporation:'))      #Current Price
SS = float(input('Enter the amount of shares you want to sell:'))           #Selling Stocks


SSV = SS*CP                   #selling Stocks values
SSB = ((SSV)/100)*2+BSB        #selling Stock Broker

SSV = str(SSV)
SSB = str(SSB)
print('You will sell for $'+SSV)
print('You will pay the commission $'+SSB)
SSV = float(SSV)
SSB = float(SSB)

Profit= SSV-SSB-(SA*BA)
if Profit > 0:
    Profit = str(Profit)
    {print('You will make a profit of $'+Profit)}
else:
    Profit=Profit*-1
    Profit = str(Profit)
    {print('You will make a loss of $'+Profit)}
