N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_x = 0
max_y = 0

min_x = int(1e9)
min_y = int(1e9)
for i in range(N):
    if max_x < arr[i][0]:
        max_x = arr[i][0]
    if min_x > arr[i][0]:
        min_x = arr[i][0]

for i in range(N):
    if max_y < arr[i][1]:
        max_y = arr[i][1]
    if min_y > arr[i][1]:
        min_y = arr[i][1]

result_x = 0
for i in range(min_x, max_x+1):
    temp_x = 0
    for j in range(len(arr)):
        if arr[j][0] <= i:
            temp_x += 1
    if temp_x == len(arr) - 1:
        result_x = i
        break

result_y = 0
for i in range(min_y, max_y+1):
    temp_y = 0
    for j in range(len(arr)):
        if arr[j][1] <= i:
            temp_y += 1
    if temp_y == len(arr) - 1:
        result_y = i
        break

print((result_x-min_x)*(result_y-min_y))