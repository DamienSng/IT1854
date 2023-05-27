prev1 = 0
prev2 = 1

print(f'{prev1}, {prev2}, ', end="")
while True:
    current = prev1 + prev2
    print(f'{current}, ', end="")
    prev1 = prev2
    prev2 = current
    if current>2000:
        break
