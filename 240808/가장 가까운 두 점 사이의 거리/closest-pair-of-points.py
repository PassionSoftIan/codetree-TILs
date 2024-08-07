N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

min_result = 1000001
for i in range(N):
    x1, y1 = arr[i][0], arr[i][1]
    for j in range(i+1, N):
        x2, y2 = arr[j][0], arr[j][1]
        result = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        min_result = min(min_result, result)

print(min_result)