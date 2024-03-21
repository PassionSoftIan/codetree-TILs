'''
1. 숫자 0과 1로만 이루어진 격자 주어짐.
2. 상 하 좌 우 인접한 칸 중 숫자 1이 적혀 있는 칸 수가 3개 이상인 곳의 개수를 구하라.


1- 내 풀이

1) N * N 크기의 배열을 입력받는다.
2) 입력받은 배열을 순서대로 탐색하며 우 하 좌 상 탐색한 뒤 갯수를 센다.
3) 세 개 이상인 칸의 경우 max_result += 1.
4) max_result를 출력한다.

'''
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            ny, nx = i + dy[k], j + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1:
                    count += 1
        if count >= 3:
            max_result += 1

print(max_result)