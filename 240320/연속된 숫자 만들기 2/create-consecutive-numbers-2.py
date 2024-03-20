'''
1. 3명이 일직선 위에 서있음.
2. 양 끝 쪽 있는 사람 중 한사람을 선택해 남은 두 사람 사이로 이동시킴.
3. 세 사람이 서 있는 위치가 연속된 숫자가 되도록 만들려고 함.
4. 연속된 수가 되기 위한 최소 이동 횟수를 구하라.


1- 내 풀이

1) A와 B 사이 거리가 1이고 B와 C사이 거리가 1이면 print(0)
2) A와 B 사이 거리가 2이거나 B와 C사이 거리가 2이면 print(1)
3) 나머지는 모두 print(2)

'''

A, B, C = map(int, input().split())

if abs(A - B) == 1 and abs(B - C) == 1:
    print(0)

elif abs(A - B) == 2 or abs(B - C) == 2:
    print(1)

else:
    print(2)