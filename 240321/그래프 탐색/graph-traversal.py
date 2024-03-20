'''
1. N개의 정점.
2. M개의 간선
3. 양방향 그래프.
4. 1번 정점에서 이동.
5. 도달할 수 있는 서로 다른 정점의 수를 구하라.

1- 내 풀이

1) 인접리스트 만들기. N + 1
2) 양방향으로 넣어주기.
3) 1번 인덱스부터 DFS.
4) 방문 마다 result += 1
5) result 출력
'''


def DFS(start):
    global result

    for node in edge[start]:
        if visited[node] != 1:
            visited[node] = 1
            result += 1
            DFS(node)

N, M = map(int, input().split())

edge = [ [] for _ in range(N+1)]

visited = [0] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)
    edge[end].append(start)

result = 0

visited[1] = 1
DFS(1)

print(result)