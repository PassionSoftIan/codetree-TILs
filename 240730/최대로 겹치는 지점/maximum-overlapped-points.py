N = int(input())

arr = [0] * 100

for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        arr[j] += 1

print(max(arr))