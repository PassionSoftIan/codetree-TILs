from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

visited[0][0] = 1

que = deque([[0, 0]])

while que:
    n, m = que.popleft()
    for k in range(4):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                que.append([ny, nx])

print(visited[N-1][M-1])