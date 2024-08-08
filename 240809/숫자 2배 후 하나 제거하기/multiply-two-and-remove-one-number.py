N = int(input())

nums = list(map(int, input().split()))

min_count = 1e9
for i in range(N):
    arr = []
    for _ in range(N):
        arr.append(nums[_])
    arr[i] *= 2
    for j in range(N):
        temp = []
        count = 0
        for k in range(N):
            if j == k:
                continue
            temp.append(arr[k])
        for l in range(N-2):
            count += abs(temp[l] - temp[l+1])
        min_count = min(min_count, count)

print(min_count)