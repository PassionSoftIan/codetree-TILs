'''
1. 2차원 좌표 평면이 있다.
2. 서로 다른 N개의 점이 주어진다.
3. x축 혹은 y축에 평행한 직선 3개를 만든다.
4. 주어진 모든 점들을 지날 수 있는지 확인한다.

1- 내 풀이

1) 좌표 평면을 나타낼 2차원 배열 arr를 만든다. (점의 위치가 0이상 10이하 이기에 11x11)
2) for nc in range(N) 순회하며 점을 좌표평면에 그린다.
2-1) 임시로 선을 그어볼 temp_arr 배열도 만들어 둔 뒤 2번 반복문이 새로 시작될 때 마다 갱신되게 한다.
3) for i in range(11)를 순회하며 1번 선을 정한다.
4) for j in range(11)를 순회하며 2번 선을 정한다.
5) for k in range(11)를 순회하며 3번 선을 정한다.
6) 선을 그릴 때는 해당 라인의 점이 != 0 일 경우 -=1을 한다.
7) 3번 째 까지 그려볼 때 마다 점을 만나면 count +=1을 하고 해당 임시 배열의 좌표는 지운다(-=1).
8) count == N이라면 맞다면 1을 출력하고 프로그램을 종료한다.
8) 만약 프로그램이 종료되지 않고 2번 반복문까지 돌았을 경우에는 0을 출력한다.
'''


def new_temp_arr():
    new_temp = [[0]*11 for _ in range(11)]

    for i in range(11):
        for j in range(11):
            new_temp[i][j] = arr[i][j]

    return new_temp


def check_x(x):

    count = 0
    for i in range(11):
        if temp_arr[i][x] != 0:
            temp_arr[i][x] = 0
            count += 1

    return count


def check_y(y):

    count = 0
    for i in range(11):
        if temp_arr[y][i] != 0:
            temp_arr[y][i] = 0
            count += 1

    return count


N = int(input())

arr = [[0]*11 for _ in range(11)]

for i in range(N):
    x, y = map(int, input().split())
    arr[y][x] = 1

for l1 in range(11):
    for l2 in range(11):
        for l3 in range(11):
            for check in range(4):
                temp_arr = new_temp_arr()

                result = 0
                if check == 0:
                    result += check_x(l1)
                    result += check_x(l2)
                    result += check_x(l3)
                if check == 1:
                    result += check_x(l1)
                    result += check_x(l2)
                    result += check_y(l3)
                if check == 2:
                    result += check_x(l1)
                    result += check_y(l2)
                    result += check_y(l3)
                if check == 3:
                    result += check_y(l1)
                    result += check_y(l2)
                    result += check_y(l3)
                
                if result == N:
                    print(1)
                    exit()

print(0)