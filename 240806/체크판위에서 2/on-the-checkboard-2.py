N, M = map(int, input().split())

arr = [list(map(str, input().split())) for _ in range(N)]

count = 0
for i in range(1, N-2):
    for j in range(1, M-2):
        if arr[0][0] == arr[i][j]:
            continue
        for k in range(i+1, N-1):
            for l in range(j+1, M-1):
                if arr[i][j] == arr[k][l] or arr[k][l] == arr[N-1][M-1]:
                    continue
                count += 1

print(count)