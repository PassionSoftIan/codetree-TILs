N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

max_count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        count = 0
        for a, b in arr:
            if (i == a and j == b) or (i == b and j == a):
                count += 1
        max_count = max(max_count, count)

print(max_count)