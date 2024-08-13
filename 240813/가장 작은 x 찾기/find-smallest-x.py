N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(5001):
    x = i
    for j in range(N):
        a, b = arr[j]
        if a <= x*2 <= b:
            x *= 2
        else:
            break
    else:
        print(i)
        break