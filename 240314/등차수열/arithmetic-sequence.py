'''
1. N개의 숫자가 주어진다.
2. 1 <= k <= 100의 수를 적절하게 정의한다.
3. 1 <= i < j < N 가 되도록 값을 설정한다.
4. arr[i] 와 k arr[j]가 등차수열이 되게 한다.
5. 등차수열일 때 result += 1을 한다.


1- 내 풀이

0) arr를 정렬한다.
1) for k in range(arr[0]+1, arr[-1]) 순회를 하며 k를 특정한다.
2) for i in range(k+1, N-1) 순회를 한다.
3) for j in range(i+1, N) 순회를 한다.
4) if k - arr[i] == arr[j] - k일 경우 count += 1을 한다.
5) 다음 k번이 되기 전 max_result와 비교하여 count가 더 크다면 교체한다.
6) max_result를 출력한다

'''

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

max_result = 0
for k in range(arr[0]+1, arr[-1]):
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if k - arr[i] == arr[j] - k:
                count += 1
    max_result = max(max_result, count)

print(max_result)