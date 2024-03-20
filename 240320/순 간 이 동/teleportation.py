'''
1. A위치에서 출발하여 B위치까지 걸어감.
2. 한 번 순간이동 사용 가능.
3. X위치에서 Y위치로 이동 가능.
4. Y위치에서 X위치로 이동 가능.
5. 걷는 거리의 최소를 구하라.

A, B, X, Y가 주어진다.


1- 내 풀이

1) A에서 B를 바로 가는 거리를 구하고 최소값이면 갱신한다.
2) A에서 X를 간 뒤 Y에서 B를 가는 거리를 구하고 최소값이면 갱신한다.
3) A에서 Y를 간 뒤 X에서 B로 가는 거리를 구하고 최소값이면 갱신한다.

'''


A, B, X, Y = map(int, input().split())

min_result = 101

min_result = min(min_result, abs(A - B))

min_result = min(min_result, abs(A - X) + abs(B - Y))

min_result = min(min_result, abs(A - Y) + abs(B - X))

print(min_result)