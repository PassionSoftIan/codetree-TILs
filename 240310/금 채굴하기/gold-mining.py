dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def search(depth, end, n, m):
    global count

    # if depth == end:
    #     return
    
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            if arr[ny][nx] == 1:
                count += 1
        if depth < end:
            search(depth+1, end, ny, nx)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    for j in range(N):
        visited = [[0] * N for _ in range(N)]
        visited[i][j] = 1
        for p in range(1, M+1):
            cost = p*p + (p+1)*(p+1)
            count = 0
            if arr[i][j] == 1:
                count += 1
            search(0, p, i, j)
            if cost <= count*5:
                max_result = max(max_result, count)

print(max_result)