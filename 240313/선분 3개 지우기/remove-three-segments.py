'''
1. N개의 선분이 1차원 직선에 주어진다.
2. 서로 다른 선분 3개를 제거한다.
3. 남은 N-3 개의 선분끼리 모두 겹치지 않을 수 있는지 확인한다.
4. 3번의 조건을 충족한다면 count를 1개 올린다.
5. 단, 경계가 닿는 경우도 겹치는 것으로 간주한다.

1- 내 풀이

1) 일차원 직선 배열을 만든다.
2) 직선 배열에 선을 긋는다. (각 a, b 범위의 index에 +=1을 한다)
3) 이후 선분 리스트에서 '각기 다른' 3개의 선을 제거한다. (범위만큼 -=1을 한다)
4) 일차원의 직선이 모두 0또는 1로 이루어져 있는지 확인한다.
5) 4번 조건을 충족한다면 count += 1을 한다.
6) count를 출력한다.
'''

def remove(l1, l2, l3):
    line_temp = [ _ for _ in line]

    x1, x2 = l1
    for rm1 in range(x1, x2+1):
        line_temp[rm1] -= 1

    x3, x4 = l2
    for rm2 in range(x3, x4+1):
        line_temp[rm2] -= 1

    x5, x6 = l3
    for rm3 in range(x5, x6+1):
        line_temp[rm3] -= 1
    
    for check in line_temp:
        if check > 1:
            return False
    
    return True

N = int(input())

line = [0] * 101

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    a, b = arr[i]

    for j in range(a, b+1):
        line[j] += 1

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if remove(arr[i], arr[j], arr[k]):
                result += 1

print(result)