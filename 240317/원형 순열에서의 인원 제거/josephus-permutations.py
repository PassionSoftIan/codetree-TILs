from collections import deque

N, K = map(int, input().split())

que = deque([ _ for _ in range(1, N+1)])

result = []
while que:
    for i in range(K-1):
        k = que.popleft()
        que.append(k)
    result.append(que.popleft())

print(*result)