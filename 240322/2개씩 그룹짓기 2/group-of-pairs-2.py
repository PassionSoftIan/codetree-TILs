'''
1. 총 N개의 그룹을 만들고자 함.
2. 2N개의 정수가 주어짐.
3. 겹치지 않으면서 2개의 원소가 하나의 그룹을 이루도록 하고자 함.
4. 그룹 내에 있는 2개의 수의 차이를 계산
5. 그룹의 차이 중 제일 작은 것이 모든 경우의 수에서 최대여야 함.

1- 내 풀이

1) 내림차순으로 정렬한다.
2) 큰 그룹과 작은 그룹 반반 나눈다.
3) 큰 그룹과 작은 그룹을 순서대로 짝 지으며 차를 구한다.
4) min_result와 비교하여 작으면 갱신한다.
5) min_result 출력.
'''

N = int(input())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

min_result = 1000000000
for i in range(N):
    min_result = min(min_result, numbers[i] - numbers[i+N])

print(min_result)