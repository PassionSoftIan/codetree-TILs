N, M = map(int, input().split())

N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))

hashmap = {}

for i in range(N):
    key = N_lst[i]
    hashmap[key] = 1

for i in range(M):
    key = M_lst[i]
    if key in hashmap:
        hashmap.pop(key)
    else:
        hashmap[key] = 1

print(len(hashmap))