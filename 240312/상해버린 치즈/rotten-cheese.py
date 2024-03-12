'''
N = 사람 수
M = 치즈 수
D = 치즈를 먹은 기록 수
S = 아팠던 기록 수

eat = 몇 번째 사람(p), 몇 번째 치즈(m), 언제 먹었는지(t초)
sick = 몇 번째 사람(p), 몇초에 확실히 아팠는지(t초)

상한 치즈는 단 하나인 것이 중요하다!

1- 내 풀이

0) 아픈사람 명단 배열을 만든다
1) 사람수 만큼 순회한다.
2) 아픈 기록 만큼 순회하며 1번에서 순회중인 사람이 명단에 있는지 체크한다.
3) 명단에 있으면 알약 개수를 올리고 아픈 사람으로 체크를 한 뒤 언제부터 아팠는지 저장한다.
4) 치즈 개수 + 1 만큼 0인 배열을 만든다(가장 바깥에)
5) 아픈 사람이 먹은 치즈를 치즈 배열에 +1을 한다
6) 다시 치즈를 먹은 기록을 돈다.
7) 해당 사람이 아픈 사람으로 체크된적이 있는지 본다.
8) 체크된 적이 없다면 해당 사람이 먹은 치즈를 확인하는데 해당 치즈 인덱스에 숫자가
아픈사람의 숫자와 일치한지 체크한다.
9) 체크한 뒤 일치한다면 알약 수를 늘린다.
9) 알약 수를 제출한다

'''


N, M, D, S = map(int, input().split())

eat = [list(map(int, input().split())) for _ in range(D)]

sick = [list(map(int, input().split())) for _ in range(S)]

cheese = [0] * (M+1)

human = [0] * (N+1)

pill = 0

for i in range(1, N + 1):
    for j in range(S):
        sick_time = 0
        if i == sick[j][0]:
            sick_time = sick[j][1]
            pill += 1
            human[i] = 1
        else:
            continue
        for k in range(D):
            if eat[k][0] != i:
                continue
            cheese_eat_time = eat[k][2]
            cheese_num = eat[k][1]
            if sick_time > cheese_eat_time:
                cheese[cheese_num] += 1


for i in range(D):
    human_num = eat[i][0]
    cheese_num = eat[i][1]
    eat_time = eat[i][2]
    if human[human_num] == 0 and cheese[cheese_num] == S:
        human[human_num] = 1
        pill += 1
print(pill)