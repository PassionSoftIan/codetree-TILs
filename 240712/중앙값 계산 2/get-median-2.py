n = int(input())

nums = list(map(int, input().split()))

temp = []

for i in range(1, n+1):
    temp.append(nums[i-1])
    if i % 2 == 1:
        temp.sort()
        print(temp[i//2], end=' ')