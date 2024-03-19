'''
1. 0, 1로 구성된 N*N 격자판이 있음.
2. 1은 폭탄이 놓일 자리.
3. 폭탄은 3가지 종류가 있음.
4. 폭탄 위치를 포함하여 파란색을 초토화시킴.(문제 사진 참고)
5. 가장 많은 영역을 초토화시키는 조합을 구하시오.


1- 내 풀이

1) 1이 들어갈 자리가 몇개인지 구한 뒤 해당 자리에 가능한 폭탄의 모든 조합을 배치해서 터트려봄.


'''


def bomb_check(bomb_num, y, x, visited):
    direction = [[(0, 0), (-1, 0), (-2, 0), (1, 0), (2,0)], [(0, 0), (0, 1), (1, 0), (0, -1), (-1,0)], [(0, 0), (1, 1), (1, -1), (-1, -1), (-1,1)]]

    for i in range(5):
        n, m = direction[bomb_num - 1][i]
        ny, nx = n+y, x+m
        if 0 <= ny < N and 0 <= nx < N:
            visited[y+n][x+m] = 1

    return visited


def explosion(depth):
    global max_result

    if depth == len(bombsite):
        visited = [[0] * N for _ in range(N)]
        for j in range(len(bombsite)):
            n, m = bombsite[j]
            bomb_num = bomb[j]
            visited = bomb_check(bomb_num, n, m, visited)
        
        result = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    result += 1
        max_result = max(max_result, result)

        return
    
    for i in range(1, 4):
        bomb.append(i)
        explosion(depth + 1)
        bomb.pop()


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0

bombsite = []
bomb = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bombsite.append([i, j])

explosion(0)

print(max_result)