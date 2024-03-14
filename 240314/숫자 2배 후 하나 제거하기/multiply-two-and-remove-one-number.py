'''
1. N개의 숫자가 주어진다.
2. N개 중 하나의 숫자를 선택한다.
3. 2에서 선택한 숫자에 2를 곱한다.
4. 다시 N개의 숫자 중 하나를 제거한다.
5. 나머지 숫자(N-1개)의 인접한 숫자간의 차가 최소가 되도록 한다.

1- 내 풀이
1) for i in range(N) 순회를 하며 해당 idx(i)에 저장된 nums 배열에 숫자 하나를 고른다.
2) 1에서 선택한 숫자에 2를 곱해 저장한다.
3) for j in range(N)와 for k in range(N)을 순회하며 i != k 일 경우 nums[k]를 temp_nums의 빈배열에 저장한다.
4) for l in range(N-2)를 순회하며 abs(temp_nums[k] - temp_nums[k+1])을 temp_result에 더한다.
5) 4번 순회가 끝난 뒤 max_result와 비교하여 더 큰 값을 max_result에 저장한다.
6) 3번 순회가 끝난 뒤 nums[i] = nums[i] // 2를 하여 값을 원복한다.
7) 1번 순회가 끝난뒤 max_result를 출력한다.

'''

N = int(input())

nums = list(map(int, input().split()))

min_result = int(1e9)
for i in range(N):
    nums[i] *= 2
    
    for j in range(N):
        temp_nums = []

        for k, elem in enumerate(nums):
            if j != k:
                temp_nums.append(elem)

        temp_result = 0
        for l in range(N-2):
            temp_result += abs(temp_nums[l+1] - temp_nums[l])
    
        min_result = min(min_result, temp_result)

    nums[i] = nums[i] // 2

print(min_result)