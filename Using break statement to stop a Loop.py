
line = input ('Enter a sentence: ')
for letter in line:
    if letter == ' ':
        continue            # stop the loop and skip to line print goodbye
    print(f'{letter}', end="")
print('Goodbye')
