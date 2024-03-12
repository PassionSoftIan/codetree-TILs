'''
N = 사람 수
M = 치즈 수
D = 치즈를 먹은 기록 수
S = 아팠던 기록 수

eat = 몇 번째 사람(p), 몇 번째 치즈(m), 언제 먹었는지(t초)
sick = 몇 번째 사람(p), 몇초에 확실히 아팠는지(t초)

상한 치즈는 단 하나인 것이 중요하다!

1- 내 풀이

0) 아픈사람 명단 배열을 만든다.
0) 아픈 사람이 먹었던 치즈를 저장할 2차원 배열을 만든다.(중복 체크를 위해)
0) 아픈 사람들이 다 먹었는지 확인할 치즈 배열을 만든다.

1) 아픈 사람의 기록 개수 만큼 순회한다.
2) 아픈 사람 명단에 올린다.
3) 치즈를 먹은 기록을 보며 아픈 사람이 먹은 치즈를 확인한다.
4) 중복을 체크하여 새롭게 봐야할 치즈라면 아픈 사람이 먹은 치즈가 아프기 이전 시점인지 확인한다.
5) 이전 시점이라면 먹은 표시를 하기 위해 치즈 배열에 개수를 하나 올린다.
6) 중복 방지를 위해 먹은 치즈를 체크 하는 배열에 해당 사람이 먹은 치즈를 넣는다.
7) 이후 다시 치즈를 먹은 기록을 보며 치즈들을 먹은 사람의 수가 아픈 사람의 수와 일치하는 치즈를
기록에 나온 사람이 먹었다면 환자명단에 올리고 알약 개수를 1개 늘린다.
'''


N, M, D, S = map(int, input().split())

eat = [list(map(int, input().split())) for _ in range(D)]

sick = [list(map(int, input().split())) for _ in range(S)]

cheese = [0] * (M+1)

human = [0] * (N+1)

cheese_check = [[] for _ in range(N+1)]

pill = 0

for i in range(S):
    human_num = sick[i][0]
    sick_time = sick[i][1]
    
    human[human_num] = 1
    pill += 1

    for k in range(D):
        if eat[k][0] != human_num:
            continue
        cheese_eat_time = eat[k][2]
        cheese_num = eat[k][1]
        if cheese_num in cheese_check[human_num]:
            continue
        if sick_time > cheese_eat_time:
            cheese[cheese_num] += 1
            human[human_num] = 1
            cheese_check[human_num].append(cheese_num)

for i in range(D):
    human_num = eat[i][0]
    cheese_num = eat[i][1]
    eat_time = eat[i][2]
    if human[human_num] == 0 and cheese[cheese_num] == S:
        human[human_num] = 1
        pill += 1
print(pill)