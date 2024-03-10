def check_col(n, m, row, col):
    count = 0
    for k in range(row):
        temp = 0
        for p in range(col):
            if 0 < arr[k][p]:
                temp += 1
            else:
                return count
        count += temp
    return count

def check_row(n, m, row, col):    
    count = 0
    for k in range(row):
        temp = 0
        for p in range(col):
            if 0 < arr[k][p]:
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

def row(n, m):
    count = 0
    for k in range(n, N):
        if 0 < arr[k][m]:
            count += 1
        else:
            return count
    return count

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = -1
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j]:
            col_count = col(i, j)
            row_count = row(i, j)
            max_result = max(max_result, check_row(i, j, row_count, col_count), check_col(i, j, row_count, col_count))


print(max_result)