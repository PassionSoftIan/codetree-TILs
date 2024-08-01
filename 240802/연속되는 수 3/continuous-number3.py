N = int(input())

arr = [int(input()) for _ in range(N)]

max_count = 0

count = 0
for i in range(N):
    if i == 0 or (arr[i-1] + abs(arr[i-1]) == 0 and arr[i] + abs(arr[i]) == 0):
        count += 1
    
    elif i == 0 or (arr[i-1] + abs(arr[i-1]) != 0 and arr[i] + abs(arr[i]) != 0):
        count += 1
    
    else:
        count = 1

    max_count = max(max_count, count)

print(max_count)