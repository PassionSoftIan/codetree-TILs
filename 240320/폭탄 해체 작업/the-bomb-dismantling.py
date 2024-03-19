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

1) 제한시간을 기준으로 내림차순 정렬한다.
2) 가장 제한 시간이 높은 순서로 거꾸로 내려온다.
3) 거꾸로 내려오며 해당 시간과 같거나 클 경우에 heapq에 넣는다.
4) 아닌 경우가 생기면 그동안 모아놓은 heapq에서 최대 값을 찾아서 max_result에 더한다.
5) max_result를 출력한다.

'''
import heapq

N = int(input())

bombs_info = []

max_time = 0

for i in range(N):
    score, time = map(int, input().split())
    max_time = max(max_time, time)
    bombs_info.append([score, time])

bombs_info.sort(key=lambda x : -x[1])


idx = 0

scores = []

max_result = 0
result = 0
while idx != N+1:
    if idx == N:
        if scores:
            max_result += -heapq.heappop(scores)
            break
    if bombs_info[idx][1] >= max_time:
        heapq.heappush(scores, -bombs_info[idx][0])
        idx += 1
    else:
        if scores:
            max_result += -heapq.heappop(scores)
        max_time -= 1

print(max_result)