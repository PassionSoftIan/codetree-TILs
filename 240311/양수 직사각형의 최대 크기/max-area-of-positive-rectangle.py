def max_sum(y1, x1, y2, x2):
    count = 0
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if 0 < arr[i][j]:
                count += 1
            else:
                return -1
    return count

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = -1
for i in range(N):
    for j in range(M):
        for l in range(i, N):
            for k in range(j, M):
                max_result = max(max_result, max_sum(i, j, l, k))
print(max_result)