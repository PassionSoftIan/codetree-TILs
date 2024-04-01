dy = [0, 1]
dx = [1, 0]


def dp_(n, m):

    for k in range(2):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0:
                if dp[ny][nx] == 1_000_001:
                    dp[ny][nx] = dp[n][m] + arr[ny][nx]
                
                else:
                    dp[ny][nx] = max(dp[ny][nx], dp[n][m] + arr[ny][nx])
                
                visited[ny][nx] = 1
                dp_(ny, nx)
                visited[ny][nx] = 0

N = int(input())

arr = [list(map(int, input().split())) 
for _ in range(N)]

visited = [[0] * N for _ in range(N)]

visited[0][0] = 1

dp = [[1_000_001] * N for _ in range(N)]

dp[0][0] = arr[0][0]

dp_(0, 0)

print(dp[N-1][N-1])