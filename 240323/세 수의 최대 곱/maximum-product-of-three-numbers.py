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
for i in range(len(plus_lst)):
    if i == 0:
        plus_result = plus_lst[i]
        plus_count += 1
    else:
        plus_result = plus_result*plus_lst[i]
        plus_count += 1
    
    if plus_count == 3:
        break

minus_result = 0
minus_count = 0
for i in range(len(minus_lst)):
    if i == 0:
        minus_result = minus_lst[i]
        minus_count += 1
    else:
        if minus_count != 2:
            minus_result = minus_result*minus_lst[i]
            minus_count += 1
        else:
            if plus_lst:
                minus_result = minus_result*plus_lst[0]
            minus_count += 1
    
    if minus_count == 3:
        break

max_result = max(max_result, plus_result, minus_result)

print(max_result)