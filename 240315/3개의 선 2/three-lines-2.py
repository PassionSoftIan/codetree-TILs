'''
1. 2차원 좌표 평면이 있다.
2. 서로 다른 N개의 점이 주어진다.
3. x축 혹은 y축에 평행한 직선 3개를 만든다.
4. 주어진 모든 점들을 지날 수 있는지 확인한다.

1- 내 풀이

1) 좌표 평면을 나타낼 2차원 배열 arr를 만든다. (점의 위치가 0이상 10이하 이기에 11x11)
2) for i in range(N) 순회하며 점을 좌표평면에 그린다.
2-1) 임시로 선을 그어볼 temp_arr 배열도 만들어 둔 뒤 2번 반복문이 새로 시작될 때 마다 갱신되게 한다.
3) for j in range(12)를 순회하며 x 축에 평행한 직선을 그릴 점을 정한다.
4) for k in range(12)를 순회하며 y 축에 평행한 직선을 그릴 점을 정한다.
5) for l in range(12)를 순회하며 3, 4번 축과 겹치지 않게 함께 그릴 3번 째 직선을 x, y 번갈아 가며 그려본다.
6) 선을 그릴 때는 해당 라인의 점이 != 0 일 경우 -=1을 한다.
7) 3번 째 까지 그려볼 때 마다 sum(arr) == 0인지 확인하고 맞다면 1을 출력하고 프로그램을 종료한다.
8) 만약 프로그램이 종료되지 않고 2번 반복문까지 돌았을 경우에는 0을 출력한다.
'''


def check(j, k, l):
    temp_arr = [ _ for _ in arr]

    temp_arr_count = 0
    third_line_count = 0

    # x축 평행선
    for i in range(11):
        if temp_arr[i][j] != 0:
            temp_arr_count += 1
    
    # y축 평행선
    for j in range(11):
        if temp_arr[k][j] != 0:
            temp_arr_count += 1

    # x축 평행선 or y축 평행선
    third_line = [ _ for _ in temp_arr]

    third_line_count = temp_arr_count

    for k in range(11):
        if temp_arr[l][k] != 0:
            temp_arr_count += 1

        if third_line[k][l] != 0:
            third_line_count += 1

    if temp_arr_count == N or third_line_count == N:
        return 1

    return 0


N = int(input())

arr = [[0]*11 for _ in range(11)]

for i in range(N):
    x, y = map(int, input().split())
    arr[y][x] = 1

#그어볼 y선
for j in range(12):
    #그어볼 x선
    for k in range(12):
        #그어볼 x선 or y선
        for l in range(12):
            if check(j, k, l) == 1:
                print(1)                
                exit()

print(0)