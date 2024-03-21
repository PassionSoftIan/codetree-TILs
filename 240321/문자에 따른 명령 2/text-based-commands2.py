'''
1. 좌표 평면 0, 0에서 시작.
2. 북쪽을 바라보고 있음.
3. N개의 명령어가 주어짐.
4. L은 반시계 90도 방향.
5. R은 시계 90도 방향.
6. F는 앞으로 이동.


1- 내 풀이

1) dy, dx를 [북, 동, 남, 서] 으로 생성.
2) 초기 방향 direction = 0 (북)으로 생성.
3) L일 경우 direction = (direction + 3) % 4
4) R일 경우 direction = (direction + 1) % 4
5) F일 경우 y = y + dy[direction], x = x + dx[direction]
6) print(x, y)

'''

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

commands = list(map(str, input()))

y, x = 0, 0

direction = 0
for command in commands:
    if command == 'L':
        direction += (direction + 3) % 4
    
    if command == 'R':
        direction += (direction + 1) % 4
    
    if command == 'F':
        y = y + dy[direction]
        x = x + dx[direction]

print(x, y)