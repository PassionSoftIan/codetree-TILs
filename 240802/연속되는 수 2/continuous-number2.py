N = int(input())

arr = [int(input()) for _ in range(N)]

max_count = 0

count = 1
for i in range(1, N):
    if arr[i-1] == arr[i]:
        count += 1
    
    else:
        max_count = max(max_count, count)
        count = 1

print(max_count)