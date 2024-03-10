def check(n, m, col):
    count = 0
    for l in range(n, N):
        temp = 0
        for p in range(col):
            if 0 < arr[l][p]:
                temp += 1
            else:
                return count
        count += temp
    return count

def col(n, m):
    count = 0
    for k in range(m, M):
        if 0 < arr[n][k]:
            count += 1
        else:
            return count
    return count

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j]:
            col_count = col(i, j)
            max_result = max(max_result, check(i, j, col_count))


print(max_result)