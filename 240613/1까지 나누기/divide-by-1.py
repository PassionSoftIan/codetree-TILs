n = int(input())

count = 0

num = 1
while n >= 1:
    count += 1
    n = n/num
    num += 1

print(count)