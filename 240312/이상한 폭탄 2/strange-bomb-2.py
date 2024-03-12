'''
1. 폭탄은 번호가 있다.
2. 같은 번호가 부여된 폭탄의 거리가 K보다 가깝다면 폭발한다.
3. 폭발 하는 폭탄 중 번호가 가장 큰 것을 출력

1- 내풀이

1) 폭탄 하나를 지정한다.
2) 지정한 폭탄과 같은 번호를 가진 폭탄을 찾는다.
3) 지정한 폭탄과 같은 번호를 가진 폭탄의 거리를 구한다.
4) 거리를 비교하여 K보다 작으면 터지는 폭탄으로 규정한다.
5) 터지는 폭탄을 포함하여 사이에 모든 폭탄들을 탐색한다.
6) 번호가 가장 큰 폭탄의 번호와 비교해서 번호가 큰 것으로 최대 폭탄의 번호를 교체한다.
7) 최대 폭탄의 번호를 출력한다.
'''

N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

max_result = -1
for i in range(N):
    for j in range(N):
        if arr[i] == arr[j]:        
            if abs(i - j) <= K:
                for k in range(i, j):
                    max_result = max(max_result, arr[k])

print(max_result)