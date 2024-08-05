N = int(input())

arr = list(map(int, input().split()))

count = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if arr[i] <= arr[j] and arr[i] <= arr[k] and arr[j] <= arr[k]:
                count += 1

print(count)