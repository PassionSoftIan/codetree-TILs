def make(row,col):
    for i in range(row):
        print('1'*col)


n, m = map(int, input().split())

make(n,m)