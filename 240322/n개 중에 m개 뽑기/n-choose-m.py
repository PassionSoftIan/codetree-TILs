'''
1. N개의 숫자가 주어진다.(1 <= N 까지 숫자)
2. M개의 숫자를 고른다.
3. 중복인 조합을 모두 제거하여 모든 경우의 수를 출력한다.

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