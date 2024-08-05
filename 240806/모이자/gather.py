N = int(input())

arr = list(map(int, input().split()))

min_dist = 10000000000

for i in range(N):
    dist = 0
    for j in range(N):
        dist += arr[j] * abs(i-j)
        
    min_dist = min(min_dist, dist)

print(min_dist)