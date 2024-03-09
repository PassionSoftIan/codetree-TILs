hy = [0, 1, 0, -1]
hx = [1, 0, -1, 0]

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]


def search(n, m, check):
    count = 0
    for hc in range(1, check + 1):
        for hk in range(4):
            hny, hnx = n + hc * hy[hk], m + hc * hx[hk]
            if 0 <= hny < N and 0 <= hnx < N:
                if arr[hny][hnx] == 1:
                    count += 1

    for dc in range(1, check):
        for dk in range(4):
            dny, dnx = n + dc * dy[dk], m + dc * dx[dk]
            if 0 <= dny < N and 0 <= dnx < N:
                if arr[dny][dnx] == 1:
                    count += 1
    return count


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


max_result = 0
for i in range(N):
    for j in range(N):
        for p in range(2 * (N - 1) + 1):
            cost = p * p + (p + 1) * (p + 1)
            gold = 0
            if arr[i][j] == 1:
                gold += 1
            gold += search(i, j, p)
            if cost <= gold * M:
                max_result = max(max_result, gold)

print(max_result)