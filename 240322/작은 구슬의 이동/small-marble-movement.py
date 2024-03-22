'''
1. N * N 격자가 있음.
2. 1개의 구슬이 격자 안에 있음.
3. 격자는 벽에 둘러싸여 있음.
4. 구슬은 1초에 한 번 움직임.
5. 구슬은 방향을 가지고 있음.
6. 벽에 부딪히면 반대로 움직임.
7. 방향을 바꾸는 데에 시간이 1만큼 소요됨.
8. T초가 지난 이후 구슬의 위치를 구하라.


1- 내 풀이

0) N, T를 입력받는다.
1) y, x, direction을 받아준다.
2) for i in range(T)반복하며 이동 혹은 방향을 바꿔준다.
3) y, x를 출력한다

'''
dy = [0, 1, -1, 0] # 오 아 위 왼
dx = [1, 0, 0, -1]


N, T = map(int, input().split())

y, x, direction = map(str, input().split())

y = int(y)
x = int(x)

direction_dict = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

for i in range(T):
    way = direction_dict[direction]
    ny, nx = y + dy[way], x + dx[way]
    if 1 <= ny < N and 1 <= nx < N:
        y = ny
        x = nx
    else:
        if direction == 'R':
            direction = 'L'
        if direction == 'L':
            direction = 'R'
        if direction == 'D':
            direction = 'U'
        if direction == 'U':
            direction = 'D'

print(y, x)