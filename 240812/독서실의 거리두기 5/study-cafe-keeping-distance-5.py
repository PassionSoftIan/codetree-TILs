N = int(input())

num = list(str(input()))

arr = [int(_) for _ in num]

max_count = 0
for i in range(N):
    if arr[i] == 0:
        arr[i] = 1
    else:
        continue
    bit = 0
    count = 0
    min_count = 100
    for j in range(N):
        if arr[j] == 1 and bit == 1:
            min_count = min(min_count, count+1)
            count = 0

        if arr[j] == 0 and bit == 1:
            count += 1
        
        if arr[j] == 1 and bit == 0:
            bit = 1
    max_count = max(max_count, min_count)
    arr[i] = 0

print(max_count)