'''
1. N개의 정수가 주어진다.
2. 연속한 부분 수열에 속한 원소들의 합이 최대일 때 값을 구하라.
3. 부분수열은 최소 한 개 이상의 원소를 포함한다.(원소가 없어서 0이 최대인 것을 만들면 안된다.)

1- 내 풀이

1) 구간 합을 저장할 temp_result = 0을 만든다.
2) 구간 합의 최대 값을 저장할 max_result = 0을 만든다.
3) for i in range(N)을 순회하며 nums[i]를 temp_result에 더한다.
4) max_result = max(max_result, temp_result)를 계속 갱신해준다.
5) temp_result가 음수가 되는 순간 0으로 바꾼 뒤 다음 수열부터 새로 시작한다.
6) 순회가 끝난 뒤 max_result를 출력한다.

'''


N = int(input())

nums = list(map(int, input().split()))

max_result = -1000 * N

temp_result = 0
for i in range(N):
    temp_result += nums[i]
    max_result = max(max_result, temp_result)

    if temp_result < 0:
        temp_result = 0

print(max_result)