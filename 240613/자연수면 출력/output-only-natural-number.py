a, b = map(int, input().split())

if 0 < a:
    for i in range(b):
        print(a, end='')
else:
    print(0)