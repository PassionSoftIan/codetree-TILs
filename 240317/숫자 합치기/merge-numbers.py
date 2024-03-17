'''
1. N개의 숫자가 주어짐.
2. 2개의 숫자를 골라 하나의 숫자로 합침.
3. 숫자가 하나 남을 때 까지 반복.
4. 이때 a, b의 숫자가 있을 경우 합치는 비용은 a+b임.
5. 최소 비용을 구하라.

1- 내 풀이

1) 우선순위 큐를 활용한다.
2) import heapq를 하여 힙을 사용한 우선순위 큐 구현을 한다.
3) pq = [] 빈 배열을 만든다.
4) pq를 우선순위큐로 만들어 nums에 있는 원소들을 우선순위 큐를 유지하며 넣는다.
5) pq에 값이 한 개 남을 때 까지 가장 작은 것들을 빼고 빠진 우선순위 큐에서 다시 또 빼서 가장 작은 값 2개를 고른다.
6) 위에서 뽑은 두 개를 a, b라 한 뒤 result += a+b를 한 뒤 다시 a+b를 우선순위 큐에 넣는다.
7) while문이 끝난 뒤 result를 출력한다.

'''
import heapq

N = int(input())

nums = list(map(int, input().split()))

pq = []
result = 0

for elem in nums:
    heapq.heappush(pq, elem)

while len(pq) != 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    result += (a + b)
    heapq.heappush(pq, a + b)

print(result)