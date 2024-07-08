def check(n, m):
    key = min(n, m)

    target = max(n, m)

    count = 1
    while True:
        go = key * count

        if go % target == 0:
            print(go)
            return
        else:
            count += 1


n, m = map(int, input().split())

check(n, m)