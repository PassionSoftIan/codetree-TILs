N = int(input())

binary = []

while True:
    if N < 2:
        binary.append(N)
        break
    
    binary.append(N % 2)

    N = N // 2

for elem in binary[::-1]:
    print(elem, end='')