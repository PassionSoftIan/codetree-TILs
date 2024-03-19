'''
1. N년 간의 자동차 가격 정보가 주어진다.
2. 자동차를 단 한 번 사서 되판다.
3. 이 때 이익을 최대화 하고자 한다.
4. 최대 이익을 출력하라.
5. 자동차를 사기 전에는 팔 수 없다.

1- 내 풀이

1) 현재 시점과 비교하여 이후 시점에 가격이 비쌀 경우만 고려한다.
2) for i in range(N)을 순회하며 시점을 구한다.
3) for j in range(i+1, N) 비교하여 i 시점 보다 더 비싼 경우 중 최대 값을 갱신한다.
4) 최대 값을 출력한다.

'''

N = int(input())

arr = list(map(int, input().split()))

max_result = 0
for i in range(N):
    for j in range(i+1, N):
        if arr[j] - arr[i] > 0:
            max_result = max(max_result, arr[j] - arr[i])

print(max_result)