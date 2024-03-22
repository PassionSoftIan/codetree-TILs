'''
1. 하나의 회의실이 있음.
2. N개의 회의 요청이 있음.
3. 각 회의 시작 끝시간 주어짐.
4. 회의가 시작되면 도중에 그만둘 수 없음.
5. 한 회의가 끝나는 직후 동시에 다른 회의 시작 가능.
6. 회의를 제일 많이 하는 경우를 구하라.


1- 내 풀이

1) 회의가 끝나는 시간으로 정렬한다.
2) 앞 회의가 끝나는 시간과 뒷 회의가 시작되는 시간이 겹치는지 확인한다.
3) 겹치면 취소해야 하는 미팅이므로 숫자를 센다.
4) 숫자를 출력한다.

'''

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x : x[1])

before_meeting_end_time = meetings[0][1]

min_result = 0
for i in range(1, N):
    if before_meeting_end_time <= meetings[i][0]:
        before_meeting_end_time = meetings[i][1]
    
    else:
        min_result += 1

print(min_result)