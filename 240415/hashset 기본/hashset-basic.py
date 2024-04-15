N = int(input())

hashset = set()

for i in range(N):
    cmd, number = map(str, input().split())
    number = int(number)

    if cmd == 'find':
        if number in hashset:
            print('true')
        else:
            print('false')
    
    if cmd == 'add':
        hashset.add(number)
    
    if cmd == 'remove':
        hashset.remove(number)