'''
1- 내 풀이

1) N명을 순회하며 한 명을 지정합니다.
2) K번 경기를 순회합니다.
3) 해당 경기에서 지정된 한명보다 순위가 높은 사람들을 차례로 넣습니다.
4) 마지막 경기에서 끝까지 순위가 한 번도 높지 않았던 사람들을 선택하여 출력합니다.

'''

K, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(K)]

result = 0
for i in range(1, N+1):
    winner = []
    for j in range(K):
        for k in range(N):
            if i == arr[j][k]:
                for l in range(0, k):
                    if arr[j][l] not in winner:
                        winner.append(arr[j][l])
                break
    
    result += (N-1) - len(winner)
print(result)