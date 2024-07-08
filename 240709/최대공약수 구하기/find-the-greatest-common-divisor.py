def check(n, m):
    key = max(n, m)

    for i in range(key, 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            exit()


n, m = map(int, input().split())

check(n, m)