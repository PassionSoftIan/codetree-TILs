'''
1. 서로다른 동전 N개가 주어짐.
2. K 금액을 완성시키기 위한 최소 동전 개수를 구하라.
3. 단, 동전은 모두 배수의 관계다.

1- 내 풀이

1) 동전이 모두 배수의 관계이기 때문에 큰 것 부터 해도 무관하다.
2) for i in range(N-1, -1, -1) 뒤에서 부터 탐색한다.
3) sum_coins = K 변수를 만든다.
4) sum_coins // coins[i]를 한 뒤 몫을 개수로 하고 coin_count += sum_coins // coins[i]을 한다.
5) sum_coins -= coins[i] * 몫 를 한다.
5) coin_count를 출력한다.

'''

N, K = map(int, input().split())

coins = [ int(input()) for _ in range(N)]

sum_coins = K
coin_count = 0
for i in range(N-1, -1, -1):
    coin_count += sum_coins // coins[i]
    sum_coins -= (sum_coins // coins[i]) * coins[i]

print(coin_count)