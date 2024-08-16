def DFS(start):
    global count

    for vertex in edge[start]:
        if visited[vertex] == 0:
            visited[vertex] = 1
            count += 1
            DFS(vertex)



N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]

visited = [0] * N

count = 0

for i in range(M):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

visited[1] = 1
DFS(1)

print(count)