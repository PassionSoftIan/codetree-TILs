N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_count = 0
for i in range(3):
    count = 0
    cup = [0, 0, 0]
    cup[i] = 1
    for j in range(N):
        a, b, c = arr[j]
        cup[a-1], cup[b-1] = cup[b-1], cup[a-1]
        if cup[c-1] == 1:
            count += 1
    max_count = max(max_count, count)

print(max_count)