'''
1. N개의 시한 폭탄 있음.
2. 각 폭탄 해체에 1시간 걸림.
3. 폭탄마다 해체 점수가 있음.
4. 각 폭탄마다 해체해야하는 시간 제한 있음.
5. 터진 폭탄은 해체 불가.(다른 폭탄 영향 X)
6. 폭탄이 다 터지거나 다 해체될 때 까지 진행.
7. 점수 최대값 구하라.

해체 점수, 시간제한

1- 내 풀이


'''


N = int(input())

bombs_info = []



for i in range(N):
    score, time = map(int, input().split())
    bombs_info.append([score, time])

bombs_info.sort(key=lambda x : (-x[0], x[1]))

max_time = 0
idx = 0

max_result = 0
while idx != N:
    if bombs_info[idx][1] >= max_time:
        max_result += bombs_info[idx][0]
        max_time += 1
        idx += 1
    else:
        idx += 1

print(max_result)