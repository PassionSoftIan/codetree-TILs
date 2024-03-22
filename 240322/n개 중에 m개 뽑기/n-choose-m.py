'''
1. N개의 숫자가 주어진다.(1 <= N 까지 숫자)
2. M개의 숫자를 고른다.
3. 중복인 조합을 모두 제거하여 모든 경우의 수를 출력한다.

1- 내 풀이

1) 1부터 N까지 숫자의 조합을 출력한다.
2) 조합이기 때문에 중복은 제거한다.
3) 자리수를 나타내줄 depth를 만든다.
4) 자리수 즉, depth가 M과 일치하면 출력한다.
5) for i in range(N+1)을 순회하며 모든 숫자를 선택한다.
6) 하지만 중복은 제거해야하기 때문에 해당 숫자에서 본인이 포함되지 않게 한다.
7) for i in range(start, N+1)을 통해 자기 자신이 선택된 이후에는 선택되지 않게 한다.
8) 이를 통해 함수의 파라미터에 start를 추가한다.
9) start는 항상 호출 될 때 마다 자기 자신을 제외한 뒤 숫자들을 포함해야한다.
10) 때문에, 함수(depth+1, i+1)로서 start에 +1을 하여 호출한다.

'''

def numbers_generator(depth, start):

    if depth == M:
        print(*numbers)
        return

    for i in range(start, N+1):
        numbers.append(i)
        numbers_generator(depth + 1, i + 1)
        numbers.pop()

N, M = map(int, input().split())

numbers = []

numbers_generator(0, 1)