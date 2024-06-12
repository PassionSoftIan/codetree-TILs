n = int(input())

count = 0

while n < 1000:
    count += 1
    if n % 2 == 0:
        n = n*3 + 1
    else:
        n = n*2 + 2

print(count)