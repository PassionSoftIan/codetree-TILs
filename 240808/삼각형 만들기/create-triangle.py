N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(N-2):
    x1, y1 = arr[i][0], arr[i][1]
    for j in range(i+1, N-1):
        x2, y2 = arr[j][0], arr[j][1]
        for k in range(j+1, N):
            x3, y3 = arr[k][0], arr[k][1]

            height = 0
            col = 0

            if x1 == x2 and y1 != y2:
                height = abs(y2 - y1)
            
            if y1 == y2 and x1 != x2:
                col = abs(x2 - x1)
            
            if x1 == x3 and y1 != y3:
                height = abs(y3 - y1)
            
            if y1 == y3 and x1 != x2:
                col = abs(x3 - x1)

            if x2 == x3 and y2 != y3:
                height = abs(y3 - y2)
            
            if y2 == y3 and x2 != x3:
                col = abs(x3 - x2)
            
            result = height*col
            max_result = max(max_result, result)

print(max_result)