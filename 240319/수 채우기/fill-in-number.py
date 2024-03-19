N = int(input())

coin_count = 0
while N != 1 and N % 5 != 0:
    N -= 2
    coin_count += 1

if N == 1:
    print(-1)
else:
    coin_count += N//5
    print(coin_count)