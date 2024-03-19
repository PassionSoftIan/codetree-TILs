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

1) 제한시간으로 정렬한다.
2) 제한시간이 같은 경우 가장 큰 값으로 바꿔준다.
3) 제한시간이 다를 경우 다시 리셋한다.
4) 마지막 점수를 더해준다.
5) max_result를 출력한다.

'''


N = int(input())

bombs_info = [list(map(int, input().split())) for _ in range(N)]

bombs_info.sort(key=lambda x : (x[1], x[0]))

max_result = 0
result = 0
now = bombs_info[0][1]
for i in range(N):
    if now == bombs_info[i][1]:
        result = max(result, bombs_info[i][0])
    else:
        max_result += result
        result = bombs_info[i][0]
        now = bombs_info[i][1]

max_result += result

print(max_result)