'''
1. 정수 N이 주어진다.
2. N개의 수가 주어진다.
3. 3개의 숫자를 적절하게 고른다.
4. 나올 수 있는 곱 중 최대를 구한다.

1- 내 풀이

1) 플러스인 숫자와 마이너스인 숫자로 나눈다.
2) 플러스인 숫자 리스트에서 가장 큰 세 숫자를 곱한다.
3) 마이너스인 숫자 중 가장 작은 값 두 개를 곱한 뒤 플러스에서 가장 큰 숫자를 곱한다.


'''

N = int(input())

numbers = list(map(int, input().split()))

plus_lst = []
minus_lst = []

for i in range(N):
    if numbers[i] < 0:
        minus_lst.append(numbers[i])
    else:
        plus_lst.append(numbers[i])

max_result = -(100000**3)

max_result = max(max_result, plus_lst[0]*plus_lst[1]*plus_lst[2], minus_lst[0]*minus_lst[1]*plus_lst[0])

print(max_result)