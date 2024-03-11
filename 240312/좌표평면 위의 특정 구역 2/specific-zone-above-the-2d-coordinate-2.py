'''
1 - 내 풀이 방법 적기 + 근거(시간복잡도, 공간복잡도, 반례가 없을지)

2 - 풀이 순서 적기
ex)
1. 입력 받기
2. 뭐 하기(예를들어 함수)
3. 뭐 하기
4. 정답 출력한다
...

'''

'''
순서대로 하나씩 빼기

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        print(j)

'''


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_x = 0
max_y = 0

min_result = int(1e9)
for i in range(N):
    max_x = 0
    max_y = 0
    min_x = int(1e9)
    min_y = int(1e9)
    for j in range(N):
        if i == j:
            continue
        if max_x < arr[j][0]:
            max_x = arr[j][0]
        if max_y < arr[j][1]:
            max_y = arr[j][1]
        if min_x > arr[j][0]:
            min_x = arr[j][0]
        if min_y > arr[j][1]:
            min_y = arr[j][1]
    min_result = min(min_result, (max_x-min_x) * (max_y-min_y))

print(min_result)