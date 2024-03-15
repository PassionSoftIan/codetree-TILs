'''
1. 새로운 틱택토 개발.
2. 원래 룰은 1대1.
3. 새로운 룰은 2명이 한 팀.
4. 게임 결과가 주어짐.
5. 팀으로 이길 수 있는 가짓 수 구하기.
6. 팀으로 이긴 것은 한 줄에 팀을 이루고 있는 2개의 숫자가 적어도 하나씩 등장해야 함.
7. 예로 111은 하나의 숫자로만 이루어져 있기 때문에 팀으로 이긴 것이 아닌 개인이 이긴 것.


1- 내 풀이

1) visited = [0] * 10 배열을 만든다.
2) 가로, 세로, 대각선을 탐방하는 3개의 함수를 만든다.
3) 탐방하며 한 줄 씩 볼 때마다 visited 해당 숫자의 idx에 +=1을 한다.
4) 3칸 순회가 끝나면 visited에 0이 아닌 idx 수를 count += 1 한다.
5) count가 2라면 팀이 이긴 것으로 간주하고 result += 1을 한다.
6) result를 출력한다.

'''


def row():

    row_result = 0
    for i in range(3):
        visited = [0] * 10
        for j in range(3):
            check = arr[j][i]
            visited[check] = 1
            
        count = 0
        temp = []
        for go in range(1, 10):
            if visited[go] == 1:
                count += 1
                temp.append(go)
        if count == 2:
            if is_duplicate(temp[0], temp[1]):
                check_duplicate.append(temp)
                row_result += 1

    return row_result


def col():

    col_result = 0
    for i in range(3):
        visited = [0] * 10
        for j in range(3):
            check = arr[i][j]
            visited[check] = 1

        count = 0
        temp = []
        for go in range(1, 10):
            if visited[go] == 1:
                count += 1
                temp.append(go)
        
        if count == 2:
            if is_duplicate(temp[0], temp[1]):
                check_duplicate.append(temp)
                col_result += 1

    return col_result


def diag():

    visited = [0] * 10

    diag_result = 0

    for i in range(2):
        visited = [0] * 10
        for j in range(3):
            if i == 0:
                check = arr[j][j]
                visited[check] = 1
            
            else:
                check = arr[j][-(j+1)]
                visited[check] = 1

        count = 0
        temp = []
        for go in range(1, 10):
            if visited[go] == 1:
                count += 1
                temp.append(go)

        if count == 2:
            if is_duplicate(temp[0], temp[1]):
                check_duplicate.append(temp)
                diag_result += 1       

    return diag_result

    return


def is_duplicate(num1, num2):

    count = 0
    for check_arr in check_duplicate:
        if num1 in check_arr and num2 in check_arr:
            count += 1
            if count == 2:
                return False
    
    return True


arr = [list(map(int, input())) for _ in range(3)]

check_duplicate = [[-1, -1]]

result = 0

result += row()
result += col()
result += diag()

print(result)