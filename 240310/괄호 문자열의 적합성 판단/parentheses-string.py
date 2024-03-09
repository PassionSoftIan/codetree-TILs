arr = list(map(str, input()))

count = 0

while arr:
    check = arr.pop()
    if check == ')':
        count += 1
    else:
        if count == 0:
            print('No')
            break
        else:
            count -= 1
else:
    if count == 0:
        print('Yes')
    else:
        print('No')