bit = 0
for i in range(5):
    num = int(input())

    if num % 3 != 0:
        break

else:
    bit = 1
    print(1)

if bit == 0:
    print(0)