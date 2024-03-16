'''
1. 정수 N이 주어짐.
2. 1부터 N까지의 수들이 '정확히 한 개씩' 들어있는 수열이 하나 주어짐.
3. 수열에서 시작 idx를 정한다.
4. 해당 idx에 들어있는 원소 값을 다시 idx로 하여 이동하는 것을 '움직임'이라고 한다.
5. 4번의 움직임을 M번 반 복 했을 때 원소 값들의 합이 최대일 경우를 구하라.

1- 내 풀이

1) for i in range(N) 순회하며 시작점(idx)를 정한다.
2) for j in range(M) 을 통해 M번 움직임을 반복한다.
3) 2번 움직임 동안 원소 값을 result += arr[idx] 한 뒤 idx = arr[idx]로 교체한다.
4) result의 값을 max_result와 비교하여 높은 것을 max_result로 갱신한다.
5) max_result를 출력한다.

'''

N, M = map(int, input().split())

arr = list(map(int, input().split()))

max_result = 0
for i in range(N):
    idx = i
    result = 0
    for j in range(M):
        result += arr[idx - 1]
        idx = arr[idx - 1]
    max_result = max(max_result, result)

print(max_result)