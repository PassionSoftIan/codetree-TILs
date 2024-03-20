'''
1. N * M 크기의 2차원 배열.
2. 좌측 상단(0, 0)에서 출발.
3. 우측 하단(N-1, M-1)에 도착.
4. 아래 오른쪽만 가능.
5. 뱀이 있는 칸 이동 X
6. 탈출 가능한지 구하라.


1- 내 풀이

1) 2차원 배열 만들기 arr = [ list(map(int, input().split())) for _ in range(N) ]
2) DFS(n, m) 시작
3) if n, m == N-1, M-1 경우 return 1
4) 아니면 return 0

'''
dy = [0, 1]
dx = [1, 0]


def DFS(n, m):

    if n == N-1 and m == M-1 and arr[n][m] == 1:
        print(1)
        exit()
    
    for k in range(2):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                DFS(ny, nx)

    print(0)
    exit()


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

DFS(0, 0)