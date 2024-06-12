n = int(input())

if n >= 3000:
    print('book')

else:
    if n >= 1000:
        print('mask')
    elif n >= 500:
        print('pen')
    else:
        print('no')