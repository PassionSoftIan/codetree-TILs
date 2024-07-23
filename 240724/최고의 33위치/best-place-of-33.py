N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

final_result = 0
for i in range(N-2):
    for j in range(N-2):
        max_result = 0
        for k in range(3):
            for p in range(3):
                if arr[i+k][j+p] == 1:
                    max_result += 1
        
        if final_result < max_result:
            final_result = max_result

print(final_result)