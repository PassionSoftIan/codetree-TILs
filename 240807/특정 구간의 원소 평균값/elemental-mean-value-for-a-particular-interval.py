N = int(input())

arr = list(map(float, input().split()))

count = 0
for i in range(N):
    for j in range(i, N):
        temp_sum = 0
        temp_count = 0
        temp_arr = []
        for k in range(i, j+1):
            temp_sum += arr[k]
            temp_count += 1
            temp_arr.append(arr[k])
        temp_avg = temp_sum / temp_count

        if temp_avg in temp_arr:
            count += 1

print(count)