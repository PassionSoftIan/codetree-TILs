n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    
    for k in range((n-i)*2):
        print(' ', end='')
    
    for p in range(i):
        print('*', end='')
    print()