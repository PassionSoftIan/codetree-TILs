N = int(input())

cmds = [list(input().split()) for _ in range(N)]

hashmap = {}

for i in range(N):
    cmd = cmds[i][0]
    key = cmds[i][1]

    if cmd == 'add':
        value = cmds[i][2]
        hashmap[key] = value
    
    if cmd == 'find':
        if key in hashmap:
            print(hashmap[key])
        
        else:
            print('None')
    
    if cmd == 'remove':
        hashmap.pop(key)