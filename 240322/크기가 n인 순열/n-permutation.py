'''
1. N개의 수가 존재.
2. 1 <= N <= 8 의 숫자로 구성. (N은 8이하로 자리수의 숫자로 봐도 무방함)
3. 숫자의 중복은 허용되지 않음.
4. 순서는 바뀔 수 있음.

1- 내 풀이.

1) 자리수를 나타낼 함수 파라미터로 depth를 만든다.
2) N이 자리수를 뜻함.
3) for i in range(1, N+1)을 하며 자리수에 해당하는 숫자를 넣는다.
4) 이때 visited[i]에 사용됐다는 표시가 있으면 넣지 않는다.
5) if depth == N일 경우 저장된 숫자를 출력한다.

'''


def permutation(depth):
    if depth == N:
        print(*number)
    
    for i in range(1, N+1):
        if visited[i] == 0:
            number.append(i)
            visited[i] = 1
            permutation(depth+1)
            number.pop()
            visited[i] = 0

N = int(input())

visited = [0] * (N+1)

number = []

permutation(0)