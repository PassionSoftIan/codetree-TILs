'''
1. 한 개의 회의실.
2. N개의 회의 요청.
3. 회의 시작 시간, 끝 시간 주어짐.
4. 회의가 도중에 중단 되는 경우는 없음.
5. 회의가 끝나는 직후 다른 회의가 시작될 수 있음.
6. 적절하게 회의 요청 수락하여 최대로 많은 회의가 진행되도록 하라.


1- 내 풀이

1) 회의가 끝나는 시간 기준으로 정렬. meeting.sort(key=lambda x : x[1])
2) 직전 회의를 항상 저장하여 비교 meeting_point 초기 값은 meeting[0][1]
3) for i in range(N) 순회를 하며 직전 회의 끝나는 시간과 비교하여 겹치지 않는다면 max_result += 1
4) 3번의 조건을 만족하면 직전 회의를 새로운 meeting_point = meeting[i][1]로 갱신
5) max_result 출력.

'''


N = int(input())

meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x : x[1])

max_result = 1

meeting_point = meeting[0][1]
for i in range(1, N):
    if meeting_point <= meeting[i][0]:
        meeting_point = meeting[i][1]
        max_result += 1

print(max_result)