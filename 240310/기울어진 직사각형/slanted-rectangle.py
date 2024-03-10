dy = [-1, -1, 1, 1]
dx = [1, -1, -1, 1]


def search(y, x, h, w):
    count = 0

    lst = [h, w, h, w]
    
    n, m = y, x
    for p in range(4):
        for u in range(1, lst[p] + 1):
            ny, nx = n + u*dy[p], m + u*dx[p]
            if 0 <= ny < N and 0 <= nx < N:
                count += arr[ny][nx]
            else:
                return 0
            if u == lst[p]:
                n, m = ny, nx
    return count


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(2, N):
    for j in range(1, N):
        for k in range(1, N):
            for l in range(1, N):
                max_result = max(max_result, search(i, j, k, l))

print(max_result)