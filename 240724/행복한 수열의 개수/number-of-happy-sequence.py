N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(N):
    temp = 1
    for j in range(N):
        if temp >= M:
            count += 1            
            break        
        if j == N-1:
            continue
        if arr[i][j] == arr[i][j+1]:
            temp += 1
        else:
            temp = 1


for i in range(N):
    temp = 1
    for j in range(N):
        if temp >= M:
            count += 1
            break
        if i == N-1:
            continue
        
        if arr[j+1][i] == arr[j][i]:
            temp += 1
        else:
            temp = 1


print(count)