N, M = map(int, input().split())

hashmap = {}

nums = list(map(int, input().split()))

check_lst = list(map(int, input().split()))

for i in range(N):
    key = nums[i]

    if key in hashmap:
        hashmap[key] += 1
    
    else:
        hashmap[key] = 1

for i in range(M):
    check_key = check_lst[i]
    if check_key in hashmap:
        print(hashmap[check_key], end=' ')
    else:
        print(0, end=' ')