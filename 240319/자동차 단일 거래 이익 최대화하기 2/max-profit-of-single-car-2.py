'''
1. N년 간의 자동차 가격 정보가 주어진다.
2. 자동차를 단 한 번 사서 되판다.
3. 이 때 이익을 최대화 하고자 한다.
4. 최대 이익을 출력하라.
5. 자동차를 사기 전에는 팔 수 없다.

1- 내 풀이(N^2) N이 10만이기 때문에 최악의 경우 100억이 되어 시간초과

1) 현재 시점과 비교하여 이후 시점에 가격이 비쌀 경우만 고려한다.
2) for i in range(N)을 순회하며 시점을 구한다.
3) for j in range(i+1, N) 비교하여 i 시점 보다 더 비싼 경우 중 최대 값을 갱신한다.
4) 최대 값을 출력한다.

2- 내 풀이(N) 10만번으로 충분히 통과할 수 있다.

1) 비교 대상 가격을 정한다. car_price = arr[0]
2) for i in range(1, N) 순회 하며 arr[i]와 car_price를 비교한다.
3) if car_price < arr[i] 일 경우 max_benefit와 arr[i] - car_price 중 더 큰 것을 최대값으로 한다.
4) else의 경우 car_price를 arr[i]로 변경한다
5) max_result를 출력한다.

'''

N = int(input())

arr = list(map(int, input().split()))

max_result = 0

car_price = arr[0]
for i in range(1, N):
    if car_price < arr[i]:
        max_result = max(max_result, arr[i] - car_price)
    
    else:
        car_price = arr[i]

print(max_result)