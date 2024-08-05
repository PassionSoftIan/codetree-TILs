char = list(input())

count = 0

for i in range(len(char) - 1):
    if char[i] != '(':
        continue
    for j in range(i+1, len(char)):
        if char[j] == ')':
            count += 1

print(count)