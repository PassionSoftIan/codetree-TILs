'''
1. N개의 숫자가 존재.
2. 숫자는 0과 1로만 존재.
3. x = 1인 위치부터 x = N인 위치까지 있음.
4. 사람이 살고 있는지 여부를 나타냄.
5. 1이면 살고 0이면 살고있지 않음.
6. 와이파이를 설치하려고 함.
7. 와이파이를 설치하면 M 거리 이하 사람까지 사용 가능.
8. 사람이 살고있지 않는 곳도 설치 가능.(범위 밖 불가)
9. 모든 사람들이 와이파이를 사용해야 하며 최소 와이파이 설치 수를 출력하라.

1- 내 풀이

1) 최소 와이파이 수를 나타낼 min_count = 0 생성.
2) 첫 idx = 0부터 탐색을 한다.
3) 사람이 살고있는 곳이 나오면 해당 사람까지 커버할 수 있는 가장 먼 곳(현재 에서  += M)에 설치한다.
4) 해당 와이파이가 커버하지 못하는 지역 부터 다시 탐색한다.(2*M + 1)
5) 설치된 와이파이를 개수를 출력한다.
'''

N, M = map(int, input().split())

people = list(map(int, input().split()))

min_count = 0
idx = 0

while idx < N:
    if people[idx] == 1:
        min_count += 1
        idx += M*2 + 1
    else:
        idx += 1

print(min_count)