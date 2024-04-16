N = int(input())

numbers_1 = set(map(int, input().split()))

M = int(input())

numbers_2 = list(map(int, input().split()))

for i in range(M):
    if numbers_2[i] in numbers_1:
        print(1, end=' ')
    else:
        print(0, end=' ')