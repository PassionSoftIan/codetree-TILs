N = int(input())

nums = list(map(int, input().split()))

nums.sort()

max_result = 0
for i in range(N):
    check = nums[i] + nums[i+N]
    if max_result < check:
        max_result = check

print(max_result)