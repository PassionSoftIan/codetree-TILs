n = int(input())

nums = list(map(int, input().split()))

temp = []

for i in range(n):
    temp.append(nums[i])
    if i % 2 == 1:
        temp.sort()
        print(temp[i//2], end=' ')

if n % 2 == 1:
    print(temp[i//2])