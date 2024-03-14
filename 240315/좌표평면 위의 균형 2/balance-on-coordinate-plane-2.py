'''
1. 좌표 평면 위에 N개의 점 존재 (점은 항상 y x가 홀수로 이루어진 좌표에 존재)
2. y점 x점을 잡고 직선 2개 그림.
3. 좌표평면 4분할.
4. 항상 직선은 짝수에 그어짐.
5. 4구역 중 점이 가장 많은 구역의 점의 수가 최소일 경우 점의 수 출력.

1- 내 풀이

1) arr 좌표 평면에 N개의 점 그리기.
2) for i in range(2, 100, 2) 짝수만 순회하며 첫번째 선 긋기(y점).
3) for j in range(2, 100, 2) 짝수만 순회하여 두번째 선 긋기(x점).
4) 2번 3번에서 나눈 구역을 탐색하고 점의 개수 count += 1
5) 구역탐색이 끝날 때 result와 count를 비교하여 큰 쪽을 새로운 result로 선정.
6) 3번 순회가 한 번씩 끝날 때 마다 min_result와 result를 비교하여 더 작은 쪽이 새로운 min_result.
7) min_result 출력

'''


def left_down(y, x):

    count = 0
    for i in range(1, y, 2):
        for j in range(1, x, 2):
            if arr[i][j] != 0:
                count += 1

    return count

def left_up(y, x):

    count = 0
    for i in range(y+1, 100, 2):
        for j in range(1, x, 2):
            if arr[i][j] != 0:
                count += 1

    return count

def right_down(y, x):

    count = 0
    for i in range(1, y, 2):
        for j in range(x+1, 100, 2):
            if arr[i][j] != 0:
                count += 1

    return count

def right_up(y, x):

    count = 0
    for i in range(y+1, 100, 2):
        for j in range(x+1, 100, 2):
            if arr[i][j] != 0:
                count += 1

    return count


N = int(input())

arr = [[0] * 101 for _ in range(100)]

for draw in range(N):
    x, y = map(int, input().split())
    arr[y][x] = 1

min_result = 101
# y점 잡고 긋기
for i in range(2, 100, 2):

    # x점 잡고 긋기
    for j in range(2, 100, 2):
        result = max(left_down(i, j), left_up(i, j), right_down(i, j), right_up(i, j))
    
        min_result = min(min_result, result)

print(min_result)