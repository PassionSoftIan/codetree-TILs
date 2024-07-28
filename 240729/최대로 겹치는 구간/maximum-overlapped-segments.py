N = int(input())

arr =[0] * 202

for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e):
        arr[j + 100] += 1

print(max(arr))