N, K = map(int, input().split())

arr = list(map(int, input().split()))

max_count = 0

for i in range(N-K+1):
    count = 0
    for j in range(K):
        count += arr[i+j]
    max_count = max(max_count, count)

print(max_count)