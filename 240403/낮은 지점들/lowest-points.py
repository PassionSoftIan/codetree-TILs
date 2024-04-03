'''
1. 2차 평면 위 N개의 점 주어짐.
2. 동일한 x 좌표를 갖는 점들에 대해 가장 작은 y 값을 갖는점만 남김.
3. 다른 점들은 전부 제거.
4. x좌표 당 최대 하나의 점만 놓여있게 만듦.
5. 남아있는 점들의 y값의 합을 구하라.


'''


N = int(input())

coordinate_list = {}

for i in range(N):
    x, y = map(int ,input().split())

    if x not in coordinate_list:
        coordinate_list[x] = y
    
    else:
        coordinate_list[x] = min(coordinate_list[x], y)

print(sum(coordinate_list.values()))