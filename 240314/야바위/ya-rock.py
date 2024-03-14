'''
1. 3개의 종이컵이 있다.
2. 안쪽이 보이지 않게 뒤집혀 있다.
3. 셋 중 하나에 조약돌을 넣는다.
4. N번에 걸쳐 a번 종이컵 b번 종이컵을 바꾼다.
5. c에 저장된 번호의 종이컵을 열어 조약돌이 있으면 count += 1을 한다.
6. 1 ~ 5를 반복하며 처음 조약돌을 어디 넣어야 가장 높은 점수를 얻을지 구하라.

a, b, c는 1 2 3 번만 가질 수 있다(종이컵은 3개 뿐이고 a != b이다.)

1- 내 풀이
1) for i in range(1, 4) 순회를 하며 조약돌을 넣을 종이컵을 선택한다.
2) cup = [0] * 4 (idx를 용이하게 하기 위해 4칸) 종이컵 배열을 만들어 해당 위치에 += 1을 하여 조약돌을 넣는다.
2) 각 경우마다 arr 배열에 저장된 셔플을 시행한다(N번)
3) 1번에서 선택해서 넣은 조약돌이 셔플할 때 마다 c에 저장된 위치에서 발견되면 count += 1을 한다.
4) 조약돌 순서가 끝날 때 마다 max_result 와 count를 비교하여 높은 쪽으로 max_result를 바꾼다.
5) max_result를 출력한다.

'''

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0
for i in range(1, 4):
    cup = [0] * 4
    cup[i] = 1

    count = 0
    for shuffle in arr:
        a, b, c = shuffle

        c_a = cup[a]
        c_b = cup[b]

        cup[a] = c_b
        cup[b] = c_a

        if cup[c] == 1:
            count += 1
    
    max_result = max(max_result, count)

print(max_result)