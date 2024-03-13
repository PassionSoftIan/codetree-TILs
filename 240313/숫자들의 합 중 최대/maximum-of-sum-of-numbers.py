'''
1. 두 개의 숫자 X, Y가 주어진다.
2. (X, Y+1) 범위를 순회한다.
3. 해당 범위에 있는 모든 수를 파싱한다.
4. 파싱된 값을 모두 더한다.

'''

X, Y = map(int, input().split())

max_result = 0
for i in range(X, Y+1):
    nums = tuple(map(int, str(i)))

    nums_sum = 0
    for j in range(len(nums)):
       nums_sum += nums[j]
    
    max_result = max(max_result, nums_sum)

print(max_result)