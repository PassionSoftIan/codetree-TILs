n, k, T = map(str, input().split())

n = int(n)
k = int(k)

string = []

for i in range(n):
    check = input()
    bit = 0
    for j in range(len(T)):
        if check[j] != T[j]:
            bit = 1
            break
    if bit == 0:
        string.append(check)

string.sort()
print(string[k-1])