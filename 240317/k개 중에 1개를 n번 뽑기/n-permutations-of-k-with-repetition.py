'''
1. 1 <= K 숫자를 하나 고르는 행위를 N번 한다.
2. 나올 수 있는 모든 서로 다른 순서쌍을 구하라.

1- 내 풀이

1) 2개를 골라야 하기 때문에 배열에 2개를 집어넣어야 한다.
2) 넣을 배열을 result = [] 로 정한다.
3) def backtracking(depth) 함수를 만든다.
4) backtracking(0)으로 실행한다고 가정한다.
5) 따라서 return 조건은 0, 1 두번이 끝난 뒤 빠져나와야 하기 때문에 종료 조건은 
6) if depth == N으로 정한다.
7) 종료 조건이 발동할 때 print(result)를 출력하나 출력 조건에 맞게 언패킹하여 출력한다.
8) print(*result)를 종료 조건에 출력하면 풀이가 끝난다.
9) 숫자를 골라야 하니 for i in range(1, K+1)으로 1이상 K이하 숫자를 고른다.
10) result.append(i)를 하여 집어 넣는다.
11) 이후에는 backtracking(depth+1) 재귀 함수를 호출한다.
12) 종료 이후 자리를 비워야 하니 result.pop()으로 자리를 만든다.

'''


def backtracking(depth):
    if depth == N:
        print(*result)
        return
    
    for i in range(1, K+1):
        result.append(i)
        backtracking(depth+1)
        result.pop()

K, N = map(int, input().split())

result = []

backtracking(0)