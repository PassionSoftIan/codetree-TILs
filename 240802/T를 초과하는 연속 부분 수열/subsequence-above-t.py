N, T = map(int, input().split())

arr = list(map(int, input().split()))

max_count = 0

count = 0

for i in range(N):
    if arr[i] > T:
        count += 1
    
    else:
        count = 0
    
    max_count = max(count, max_count)

print(max_count)