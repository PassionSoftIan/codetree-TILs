'''
1 - 내 풀이

1) 세 점을 구해야 하기 때문에 for문 3개를 돌며 체크
2) 내가 선택한 점과 for 문 2개를 돌며 만나는 점들을 비교하여 x좌표 혹은 y좌표가 같은지 확인
3) 중복 제거를 위해 i == j continue, i == k or j == k continue를 한다.
3) x좌표가 같은 점과 y좌표가 같은 점을 선택하여 계산한 뒤 가장 넓은 결과 값을 갱신한다

'''
def cal(x1, y1, x2, y2, x3, y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))


N = int(input())

arr = [list(map(int ,input().split())) for _ in range(N)]

max_result = 0
for i in range(N):
    x1, y1 = arr[i][0], arr[i][1]
    for j in range(N):
        if i == j:
            continue
        
        x2, y2 = arr[j][0], arr[j][1]
        if x1 != x2:
            continue
                
        for k in range(N):
            if i == k or j == k:
                continue

            x3, y3 = arr[k][0], arr[k][1]
            if y1 != y3:
                continue
            
            max_result = max(max_result, cal(x1, y1, x2, y2, x3, y3))

print(max_result)