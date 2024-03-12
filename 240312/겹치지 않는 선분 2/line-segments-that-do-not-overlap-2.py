'''
1- 내 풀이

1) 기준점이 되는 x1의 값과 x2의 배열 내 비교값으로 확인할 좌표들이 x1 보다는 크고 x2 보다는 작은지 확인해야한다.
2) 기준점과 비교값이 동일하지 않은 경우 탐색을 실시한다.
3-1) 비교값이 만약 x1 보다는 크고 x2 보다는 작은 경우라면 개수를 올려준 뒤 반복문을 빠져나온다.
3-2) 비교값이 만약 x1 보다 작고 x2 보다는 큰 경우라면 개수를 올려준 뒤 반복문을 빠져나온다.
4) 최종 값을 결과로 출력한다.
'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * (N+1)

result = 0
for i in range(N):

    x1, x2 = arr[i][0], arr[i][1]
    
    for j in range(N):
        if i == j or visited[j] == 1:
            continue
    
        x3, x4 = arr[j][0], arr[j][1]

        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            result += 1
            break

print(result)