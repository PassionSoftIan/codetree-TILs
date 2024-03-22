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
2) for i in range(N) 순회하며 사람이 있으면 person += 1을 한다.
3) person 숫자가 M과 같으면 와이파이를 설치한다. min_count += 1
4) person 숫자를 초기화한다.
5) min_count를 출력한다.

'''

N, M = map(int, input().split())

people = list(map(int, input().split()))

min_count = 0
person = 0
for i in range(N):
    if people[i] == 1:
        person += 1
    
    if person == M+1:
        min_count += 1
        person = 0

    if i == N-1 and person != 0:
        min_count + 1

print(min_count)