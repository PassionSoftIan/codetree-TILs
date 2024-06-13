n = int(input())

bit = 0
count = 1
for i in range(1, 2*n):
    print('*' * count)
    print()

    if bit == 0 and count >= n:
        bit = 1

    if bit == 0:
        count += 1
    else:
        count -= 1