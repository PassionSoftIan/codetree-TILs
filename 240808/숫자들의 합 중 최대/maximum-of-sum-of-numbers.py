X, Y = map(int, input().split())

max_result = 0
for i in range(X, Y+1):
    result = 0
    num = i
    while num:
        result += num % 10
        num = num // 10
    max_result = max(max_result, result)

print(max_result)