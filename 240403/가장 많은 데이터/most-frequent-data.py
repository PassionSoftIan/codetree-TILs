N = int(input())

hashmap = {}

for i in range(N):
    key = input()

    if key not in hashmap:
        hashmap[key] = 1
    
    else:
        hashmap[key] += 1

print(max(hashmap.values()))