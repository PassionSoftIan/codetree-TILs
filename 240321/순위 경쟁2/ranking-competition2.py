'''
1. 2명의 학생 A, B가 있음.
2. 각자 게임을 함.
3. 게임 결과에 따라 점수를 얻을 수 있음.
4. 점수를 잃을 수도 있음.
5. 게임 점수가 바뀔 때 마다 점수가 1등인 사람들을 모아 명예의 전당에 올림.
6. 점수 변동 관련 정보가 주어질 때 명예의 전당에 올라간 사람의 조합이 총 몇 번 바뀌는가?



1- 내 풀이

1) A_score와 B_score 생성.
2) checker = 0를 만들어 A와 B의 관계를 설정한다.
3) A > B 는 checker = -1
4) A < B 는 checker = 1
5) A = B 는 checker = 0
6) 게임을 진행할 때 마다 checker를 확인하여 변경이 있는지 확인한다.
7) 변경할 때 마다 result += 1을 해준다.
8) result를 출력한다.

'''

N = int(input())

result = 0

A_score = 0
B_score = 0
checker = 0
for i in range(N):
    user, score = map(str, input().split())

    score = int(score)

    if user == 'A':
        A_score += score


    else:
        B_score += score
    
    if A_score > B_score:
        if checker != -1:
            checker = -1
            result += 1
    
    if A_score < B_score:
        if checker != 1:
            checker = 1
            result += 1
    
    if A_score == B_score:
        if checker != 0:
            checker = 0
            result += 1

print(result)