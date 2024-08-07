N, C, G, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0


for j in range(1001):
    result =0
    for i in range(N):
        Ta, Tb = arr[i]
        if j <Ta:
            result += C
        
        if Ta <= j <= Tb:
            result += G
        
        if Tb < j:
            result += H
        
    max_result = max(max_result, result)

print(max_result)