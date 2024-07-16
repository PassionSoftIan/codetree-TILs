N = int(input())

lst = []

for i in range(N):
    cmd = list(input().split())
    key = cmd[0]

    if key == 'push_back':
        lst.append(int(cmd[1]))
    if key == 'get':
        print(lst[int(cmd[1])- 1])
    if key == 'size':
        print(len(lst))
    if key == 'pop_back':
        lst.pop()