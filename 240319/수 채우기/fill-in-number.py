'''
1. 2원과 5원을 이용하여 N을 만들고자 한다.
2. 사용되는 동전 개수가 최소로 몇개 사용되는가.


1- 내 풀이

1) coint_count = 0을 만들어 사용되는 동전 개수를 센다.
2) N이 1이 아니거나 5의 배수가 아닐 때 까지 2를 빼준다.
3) 5의 배수가 되어 while문을 빠져나오면 5를 나눠준 만큼 coin_count에 더해준다.
4) 1일 경우에는 -1을 프린트 한다.
5) 4번이 아닐 경우 coin_count를 프린트한다.

'''


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