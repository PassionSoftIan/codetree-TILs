N, key = map(int, input().split())

changed = []

while True:
    if N < key:
        changed.append(N)
        break
    
    changed.append(N % key)

    N = N // key

for elem in changed[::-1]:
    print(elem, end='')