N = int(input())

arr = [0] * 202

start = 101

for i in range(N):
    go, cmd = map(str, input().split())
    go = int(go)

    if cmd == 'R':
        for j in range(go):
            arr[start + j] += 1
        start += go

    if cmd == 'L':
        for j in range(1, go+1):
            arr[start - j] += 1
        start -= go

count = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        count += 1

print(count)