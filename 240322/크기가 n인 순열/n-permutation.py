'''
1. N개의 수가 존재.
2. 1 <= N 의 숫자로 구성.
3. 숫자의 중복은 허용되지 않음.
4. 순서는 바뀔 수 있음.

1- 내 풀이.

'''


def permutation(depth):
    if depth == N:
        print(*number)
    
    for i in range(1, N+1):
        if i not in number:
            number.append(i)
            permutation(depth+1)
            number.pop()

N = int(input())

number = []

permutation(0)