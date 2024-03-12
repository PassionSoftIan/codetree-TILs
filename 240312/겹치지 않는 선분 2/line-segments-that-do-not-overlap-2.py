'''
1- 내 풀이

1) 기준점이 되는 x1의 값과 x2의 배열 내 비교값으로 확인할 좌표들이 x1 보다는 크고 x2 보다는 작은지 확인해야한다.
2) 기준점과 비교값이 동일하지 않거나 겹친다는 방문체크가 되지 않는 경우 탐색을 실시한다.
2) 비교값이 만약 x1 보다는 크고 x2 보다는 작은 경우라면 방문체크를 한 뒤 개수를 올려준다.
3) 비교값을 모두 확인하고 난 뒤 만약 개수가 0개가 아니라면 본인도 방문체크를 한 뒤 개수를 한 개 더 올려준다.
4) 2번과 3번에서 계산한 개수를 최종 값에 더해준다.
3) 최종 값에 더한 뒤 값을 결과로 출력한다.
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * (N+1)

result = 0
for i in range(N):

    x1, x2 = arr[i][0], arr[i][1]
    
    count = 0
    for j in range(N):
        if i == j or visited[j] == 1:
            continue
    
        x3, x4 = arr[j][0], arr[j][1]

        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            visited[j] = 1
            count += 1
    if count != 0:
        visited[i] = 1
        result += count + 1

print(result)