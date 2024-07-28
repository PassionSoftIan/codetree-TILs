N, K = map(int, input().split())

arr = [0] * N

for i in range(K):
    s, e = map(int, input().split())
    for j in range(s-1, e):
        arr[j] += 1

print(max(arr))