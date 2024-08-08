# N = int(input())

# nums = list(map(int, input().split()))

# min_count = 1e9
# for i in range(N):
#     arr = []
#     for _ in range(N):
#         arr.append(nums[_])
#     arr[i] *= 2
#     for j in range(N):
#         temp = []
#         count = 0
#         for k in range(N):
#             if j == k:
#                 continue
#             temp.append(arr[k])
#         for l in range(N-2):
#             count += abs(temp[l] - temp[l+1])
#         min_count = min(min_count, count)

# print(min_count)

N = int(input())
nums = list(map(int, input().split()))

min_count = 1e9
for i in range(N):
    nums[i] *= 2  # 두 배로 증가시킴

    for j in range(N):
        count = 0
        prev = -1  # 이전 숫자를 추적하기 위한 변수

        for k in range(N):
            if j == k:
                continue
            if prev != -1:
                count += abs(nums[k] - prev)
            prev = nums[k]

        min_count = min(min_count, count)

    nums[i] //= 2  # 원래 값으로 복구

print(min_count)