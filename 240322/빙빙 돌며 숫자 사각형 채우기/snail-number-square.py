'''
1. N * M 크기의 직사각형에 숫자 1부터 순서대로 증가시킨다.
2. 벽을 만나거나 숫자를 넣은 곳을 만나면 시계방향으로 회전한다.
3. 숫자를 다 채운 격자를 출력하라.


1- 내 풀이

1) N * M 2차원 배열로 격자를 만든다.
2) 0, 0 숫자를 1로 채운다.
3) N * M의 격자 개수에서 미리 채운 1을 뺀 만큼 숫자를 넣어야 한다.
4) for i in range(2, N*M+1) 순회한다.
5) 범위를 벗어나거나 격자에 숫자가 있다면 시계방향 90도 회전한다.
6) 격자를 출력한다.

'''
dy = [0, 1, 0, -1] # 오 아 왼 위
dx = [1, 0, -1, 0]


N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

arr[0][0] = 1

y, x = 0, 0

direction = 0
for i in range(2, N*M+1):
    ny, nx = y + dy[direction], x + dx[direction]

    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
        arr[ny][nx] = i
        y, x = ny, nx
    
    else:
        direction = (direction + 1) % 4
        ny, nx = y + dy[direction], x + dx[direction]
        arr[ny][nx] = i
        y, x = ny, nx
    
for i in arr:
    print(*i)