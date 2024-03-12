'''
1 - 내 풀이 방법
1) 먼저 배열을 순차적으로 확인한다.
2) 확인할 때 하나를 고정을 하고 나머지와 비교한다.
3) (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) 계산을 한다.
4) 가장 짧은 결과를 반환한다.
'''
def cal(x1, y1, x2, y2):
    result = (abs(x1-x2)**2) + (abs(y1-y2)**2)
    return result

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

min_result = 2000000
for i in range(N):
    for j in range(i+1, N):
        min_result = min(min_result, cal(arr[i][0], arr[i][1], arr[j][0], arr[j][1]))

print(min_result)