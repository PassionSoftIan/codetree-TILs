'''
1. A와 B가 카드게임을 하고 있다.
2. 1부터 2N까지 번호가 쓰인 카드가 한 장씩 있다.
3. A와 B가 반 반씩 나눠 가진다
4. A와 B가 한 번에 카드 한 장씩을 낸다.
5. 카드 번호가 큰 사람이 점수 1점을 얻는다.
6. 카드는 한 턴에 한 번만 낸다.
7. 모든 카드를 다 낼 때 까지 반복한다.(N번)
8. B가 카드를 내는 순서가 주어져있다.
9. A가 얻을 수 있는 점수의 최대값을 구하라.


1- 내 풀이(N)

1) B_cards_seq를 정렬한다.
2) 비교할 카드를 정하고 시작점은 0번 인덱스로 하여 B_card = 0을 만든다.
3) for i in range(1, (2*N) + 1)를 반복하면서 B_cards_seq[B_card]와 비교한다.
4) i가 크다면 B_cards_seq += 1을 한다.
5) 반복문이 끝난 뒤 B_card를 출력한다.

'''


N = int(input())

B_cards_seq = [ int(input()) for _ in range(N)] 

B_cards_seq.sort()

B_card = 0
for i in range(1, (2*N)+1):
    if B_cards_seq[B_card] < i:
        B_card += 1

print(B_card)