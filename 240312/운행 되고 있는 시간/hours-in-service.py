'''
1- 내 풀이

1) 예시와 같은 개념.
2) 제외 할 기준 점을 잡음.
3) 이후 반복문을 통해 앞서 잡은 기준점을 제외한 뒤 나머지를 모두 완전 탐색.
4) 시간을 선으로 만들어줄 배열 생성.
5) 각 사람마다 출근 시간 이상, 퇴근 시간 미만의 기간을 배열에 += 1.
6) 최적화를 위해 동시에 최소 시작점, 최대 끝 지점을 저장.
7) 배열을 순회하며 0이 아닌 것들의 개수를 계산.
8) 최댓값과 비교하여 크다면 최댓값을 갱신.
9) 모든 탐색이 끝난 뒤 최댓값 반환.
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):

    sum_result = [0] * 1001
    
    start_point = 1001
    end_point = 0
    for j in range(N):
        # i를 기준점으로 잡고 i가 빠질 사람이기에 두 번째 for문에서 기준 점 사람을 뺄 때 마다 나머지를 확인 완전탐색.
        if i == j:
            continue

        # sum_result 배열 탐색 최적화를 위해 최소지점 끝지점을 구해놓음
        start_point = min(start_point, arr[j][0])
        end_point = max(end_point, arr[j][1])
        
        # 출 퇴근 시간의 차를 더하기
        for k in range(arr[j][0], arr[j][1]):
            sum_result[k] += 1
    
    # sum_result 배열에서 운행중인 시간대를 모두 체크
    count = 0
    for l in range(start_point, end_point):
        if sum_result[l] != 0:
            count += 1

    max_result = max(max_result, count)

print(max_result)