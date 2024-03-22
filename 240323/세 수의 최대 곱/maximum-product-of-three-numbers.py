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

plus_lst.sort(reverse=True)
minus_lst.sort()

max_result = -(100000**3)

plus_result = 0
plus_count = 0
if len(plus_lst) >= 3:
    for i in range(3):
        if i == 0:
            plus_result = plus_lst[i]
            continue
        else:
            plus_result = plus_result*plus_lst[i]
else:
    for i in range(len(plus_lst)):
        if plus_result == 0:
            plus_result = plus_lst[i]
        else:
            plus_result = plus_result * plus_lst[i]
        plus_count += 1
    for i in range(1, 3-plus_count+1):
        plus_result = plus_result * minus_lst[-i]

minus_result = 0
if len(minus_lst) >= 2:
    if len(plus_lst) >= 1:
        minus_result = minus_lst[0] * minus_lst[1] * plus_lst[0]
    else:
        minus_result = minus_lst[-1] * minus_lst[-2] * minus_lst[-3]

elif len(minus_lst) == 1:
    minus_result = minus_lst[0] * plus_lst[-1] * plus_lst[-2]

max_result = max(max_result, plus_result, minus_result)

print(max_result)