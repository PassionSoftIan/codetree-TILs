N = int(input())

arr = [int(input()) for _ in range(N)]

max_count = 0

count = 0
for i in range(N):
    if i == 0 or arr[i-1] == arr[i]:
        count += 1
    
    else:
        max_count = max(max_count, count)
        count = 1

print(max_count)