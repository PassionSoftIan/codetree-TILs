N = int(input())

string = [ input() for _ in range(N)]

string.sort()

for i in string:
    print(i)