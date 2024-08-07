arr = list(map(int, input().split()))

sum_arr = sum(arr)

min_count = 3000001

for i in range(4):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            if abs((sum_arr - (arr[i]+arr[j]+arr[k])) - (arr[i]+arr[j]+arr[k])) < min_count:
                min_count = abs((sum_arr - (arr[i]+arr[j]+arr[k])) - (arr[i]+arr[j]+arr[k]))

print(min_count)