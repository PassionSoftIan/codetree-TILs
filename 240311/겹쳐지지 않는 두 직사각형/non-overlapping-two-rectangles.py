def max_check(y1, x1, y2, x2):
    max_sum = -10000000
    for i in range(N):
        for j in range(M):
            for l in range(i, N):
                for k in range(j, M):
                    if not duplication_check(y1, x1, y2, x2, i, j, l, k):
                        max_sum = max(max_sum, sum_rect(y1, x1, y2, x2) + sum_rect(i, j, l, k))
    return max_sum

def sum_rect(y1, x1, y2, x2):
    count = 0
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            count += arr[i][j]
    return count

def duplication_check(y1, x1, y2, x2, y3, x3, y4, x4):
    visited = [[0]*M for _ in range(N)]
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            visited[i][j] = 1
    for l in range(y3, y4+1):
        for k in range(x3, x4+1):
            if visited[l][k] != 0:
                return True
    return False

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = -10000000
for i in range(N):
    for j in range(M):
        for l in range(i, N):
            for k in range(j, M):
                max_result = max(max_result, max_check(i, j, l, k))

print(max_result)