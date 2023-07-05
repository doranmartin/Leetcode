steps = 0

num = int(14)

while num != 0:
    if num % 2 == 0:
        num /= 2
    else:
        num -= 1

    steps += 1
    
print(steps)
