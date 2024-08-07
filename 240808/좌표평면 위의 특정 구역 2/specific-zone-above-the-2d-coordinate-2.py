N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

min_result = 1e9
for i in range(N):
    min_x = 1e9
    max_x = 0

    min_y = 1e9
    max_y = 0
    for j in range(N):
        if i == j:
            continue
        x, y = arr[j][0], arr[j][1]
        min_x = min(min_x, x)
        max_x = max(max_x, x)

        min_y = min(min_y, y)
        max_y = max(max_y, y)
    result = (max_x - min_x) * (max_y - min_y)
    min_result = min(min_result, result)

print(min_result)