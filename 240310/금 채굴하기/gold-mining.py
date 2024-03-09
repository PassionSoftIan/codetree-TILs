dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

dl = [(1, -1), (-1, -1), (-1, 1), (1, 1)]


def point_set(n, m, length):
    for k in range(4):
        ny, nx = n + length*dy[k], m + length*dx[k]
        point_lst.append([k, ny, nx])


def search(p_lst, length):
    count = 0
    while p_lst:
        d, n, m = p_lst.pop()
        for l in range(length):
            ny, nx = n + l*dl[d][0], m + l*dl[d][1]
            if 0 <= ny < N and 0 <= nx < N:
                count += arr[ny][nx]
    return count


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    for j in range(N):
        gold = arr[i][j]
        for p in range(2*(N-1) + 1):
            cost = p*p + (p+1)*(p+1)
            if p != 0:
                point_lst = []
                point_set(i, j, p)

                gold += search(point_lst, p)

            if cost <= gold*M:
                max_result = max(max_result, gold)

print(max_result)