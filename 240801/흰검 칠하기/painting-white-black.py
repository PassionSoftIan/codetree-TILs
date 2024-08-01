'''
1. N번의 명령에 걸쳐 움직임.
2. x L의 경우 왼쪽으로 이동하며 현재 위치 포함 총 x칸의 타일을 흰색으로 칠함.
3. x R의 경우 오른쪽으로 이동하며 현재 위치 포함 총 x칸의 타일을 검정으로 칠함.
4. 명령 후에는 마지막으로 칠한 타일에 서있다 가정.
5. 색이 덧칠해지면 마지막으로 칠해진 색으로 바뀜.

6. 다만, 흰색과 검은색으로 각각 2번 이상씩 칠해지면 회색으로 바뀌고 고정.

7. 흰, 검, 회 타일 수 각각 출력하라.



'''

N = int(input())

arr = [[0, 0, 0] for _ in range(50)]

start = 25

w = 0
b = 0
g = 0

for i in range(N):
    go, cmd = map(str, input().split())
    go = int(go)

    if cmd == 'R':
        for j in range(go):
            if arr[start + j][2] == 3:
                continue
            if arr[start + j][0] >= 2 and arr[start +j][1] >= 1:
                arr[start + j][2] = 3
                if arr[start + j][2] == 2:
                    b -= 1
                else:
                    w -= 1
                g += 1
            elif arr[start + j][2] == 1:
                arr[start + j][2] = 2
                arr[start + j][1] += 1
                b += 1
                w -= 1

            elif arr[start + j][2] == 2:
                arr[start + j][1] += 1
            
            else:
                arr[start + j][2] = 2
                arr[start + j][1] += 1
                b += 1
        
        start += (go-1)
    
    else:
        for j in range(go):
            if arr[start - j][2] == 3:
                continue
            if arr[start - j][0] >= 1 and arr[start - j][1] >= 2:
                arr[start - j][2] = 3
                if arr[start - j][2] == 1:
                    w -= 1
                else:
                    b -= 1
                g += 1
            elif arr[start - j][2] == 2:
                arr[start - j][2] = 1
                arr[start - j][0] += 1
                b -= 1
                w += 1

            elif arr[start - j][2] == 1:
                arr[start - j][0] += 1

            else:
                arr[start - j][2] = 1
                arr[start - j][1] += 1
                w += 1
        
        start -= (go-1)

print(w, b, g)