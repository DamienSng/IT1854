x = 'Thank'
y = 'You'


# concatenation of string x and y which is treated as a single element and then 
# printed (Here, only a single argument is passed to the print function).
print(x+y)  
# Output: ThankYou  (Simple String concatenation)


# Here, two different arguments are passed to the print function.
print(x,y)  
# Output python 2: ('Thank', 'You')  (x and y are treated as tuple
# Output python 3: Thank You  (x and y are comma seperated and hence, 
# considered two different elements - the default 'sep=" "' is applied.)


# The concatenated result of (x + y) is printed 5 times.
print((x+y)*5) 
# Output: ThankYouThankYouThankYouThankYouThankYou  

# x and y are made elements of a tuple and the tuple is printed 5 times.
print((x,y)*5) 
# Output: ('Thank', 'You', 'Thank', 'You', 'Thank', 'You', 'Thank', 'You', 'Thank', 'You')  
