N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(N):
    temp = 1
    for j in range(N):
        
        if j == N-1:
            continue
        if arr[i][j] == arr[i][j+1]:
            temp += 1
        else:
            temp = 1
        if temp >= M:
            count += 1            
            break

for i in range(N):
    temp = 1
    for j in range(N):
        if i == N-1:
            continue
        
        if arr[j][i] == arr[j][i+1]:
            temp += 1
        else:
            temp = 1
        if temp >= M:
            count += 1
            break

print(count)