def find(r, c):
    count = 0
    for p in range(r+1):
        for u in range(c+1):
            if 0 <= arr[p][u]:
                count += 1
            else:
                return 0
    return count


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    for j in range(M):
        for k in range(i, N):
            for l in range(j, M):
                max_result = max(max_result, find(k, l))

print(max_result)