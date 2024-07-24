def left(n, m):

    temp_giyeok = 0
    temp_re_giyeok = 0
    temp_nieun = 0
    temp_re_nieun = 0

    for i in range(3):
        if i == 0:
            temp_giyeok += arr[n][m]
        
        elif i == 1 and m + 1 < M:
            temp_giyeok += arr[n][m+1]
        
        elif i == 2 and (n + 1 < N and m + 1 < M):
            temp_giyeok += arr[n+1][m+1]
        
        else:
            temp_giyeok = 0
            break

    for i in range(3):
        if i == 0:
            temp_re_giyeok += arr[n][m]
        
        elif i == 1 and m - 1 >= 0:
            temp_re_giyeok += arr[n][m-1]
        
        elif i == 2 and (n + 1 < N and m - 1 >= 0):
            temp_re_giyeok += arr[n+1][m-1]
        
        else:
            temp_re_giyeok = 0
            break
    
    for i in range(3):
        if i == 0:
            temp_nieun += arr[n][m]
        
        elif i == 1 and n + 1 < M:
            temp_nieun += arr[n+1][m]
        
        elif i == 2 and (n + 1 < N and m + 1 < M):
            temp_nieun += arr[n+1][m+1]

        else:
            temp_nieun = 0
            break

    for i in range(3):
        if i == 0:
            temp_re_nieun += arr[n][m]
        
        elif i == 1 and n + 1 < M:
            temp_re_nieun += arr[n+1][m]
        
        elif i == 2 and (n + 1 < N and m - 1 >= 0):
            temp_re_nieun += arr[n+1][m-1]

        else:
            temp_re_nieun = 0
            break
    
    return max(temp_giyeok, temp_nieun, temp_re_giyeok, temp_re_nieun)

def right(n, m):

    temp_col = 0
    temp_row = 0

    for i in range(3):
        if m + i == M:
            temp_col = 0
            break
        
        else:
            temp_col += arr[n][m + i]
    
    for i in range(3):
        if n + i == N:
            temp_row = 0
            break
        
        else:
            temp_row += arr[n + i][m]
    
    return max(temp_col, temp_row)



N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0

for i in range(N):
    for j in range(M):
        max_result = max(max_result, left(i, j), right(i, j))

print(max_result)