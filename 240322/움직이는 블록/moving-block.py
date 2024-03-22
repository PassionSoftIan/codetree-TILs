'''
1. N개의 블럭 위치 존재.
2. 각 위치별로 블럭의 개수가 주어짐.
3. 특정 위치를 골라 해당 위치의 블력을 다른 위치로 옮김.
4. 작업을 반복하여 모든 위치에 놓인 블럭 개수 동일하게 만듦.
5. 움직여야할 최소 블럭 수를 구하라.


1 - 내 풀이

1) 이동해야 할 블럭 수를 나타내는 min_count 생성.
2) for i in range(N) 돌면서 되어야 하는 수보다 작으면 차이만큼 min_count에 더하기.
3) print(min_count)

'''

N = int(input())

blocks = [int(input()) for _ in range(N)]

min_count = 0

should = sum(blocks) // N

for i in range(N):
    if blocks[i] < should:
        min_count += should - blocks[i]

print(min_count)