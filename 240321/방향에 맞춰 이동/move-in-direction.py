'''
1. (0, 0)에서 시작하여 총 N번 움직임.
2. N번에 걸쳐 움직이려는 방향과 움직일 거리 주어짐.
3. 최종 위치를 출력하라.


1- 내 풀이

1) 첫 시작점 y, x = 0, 0 만들어줌.
2) for i in range(N)순회하며 input data를 문제에 맞게 잘 처리해줌.
3) print(y, x)

'''


N = int(input())

y, x = 0, 0

for i in range(N):
    direction, distance = map(str, input().split())

    distance = int(distance)
    if direction == 'E':
        x += distance
    
    if direction == 'S':
        y -= distance
    
    if direction == 'W':
        x -= distance
    
    if direction == 'N':
        y += distance

print(x, y)