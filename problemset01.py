count = 0
total = 0
while count < len(s)-2:
    word = s[count:count+3]
    if word == 'bob':
        total += 1
    count += 1
print('Number of times bob occurs is: ' +str(total))