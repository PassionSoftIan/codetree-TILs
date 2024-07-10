binary = list(map(int, input()))

result = 0

key = 0
for elem in binary[::-1]:
    if elem == 1:
        result += 2**key
    key += 1

print(result)