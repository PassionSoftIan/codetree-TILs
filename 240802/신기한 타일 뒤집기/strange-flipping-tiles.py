'''
1. 일직선 회색 타일.
2. 왼쪽으로 뒤집으면 흰색.
3. 오른쪽으로 뒤집으면 검은색
4. x L은 왼쪽으로 이동하며 현재 위치 포함 왼쪽으로 뒤집기.
5. x R은 오른쪽으로 이동하며 현재 위치 포함 오른쪽으로 뒤집기.

'''

N = int(input())

arr = [0] * 100002

start = 100002//2

for i in range(N):
    go, cmd = map(str, input().split())
    go = int(go)

    if cmd == 'L':
        for i in range(go):
            arr[start - i] = 1
        start -= (go-1)
    
    else:
        for i in range(go):
            arr[start + i] = 2
        start += (go-1)

w = 0
b = 0

for i in range(len(arr)):
    if arr[i] == 1:
        w += 1
    
    elif arr[i] == 2:
        b += 1

print(w, b)