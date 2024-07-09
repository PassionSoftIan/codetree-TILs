def change(n, m):
    n, m = m, n

    return n, m

n, m = map(int, input().split())

n, m = change(n, m)

print(n, m)