N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_count = 0

for i in range(N):
    for j in range(N-2):
        count = 0
        for k in range(3):
            if arr[i][j+k] == 1:
                count += 1
        max_count = max(max_count, count)

print(max_count)