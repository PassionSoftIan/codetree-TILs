'''
N = 장비의 개수
C, G, H = 온도에 따른 장비들의 작업량
Ta, Tb = 온도의 범위

1. 데이터 센터 온도를 맞추려고 함.
2. 장비마다 선호하는 온도의 범위가 전부 다름.
3. 각 장비의 선호하는 온도의 범위가 주어짐.
4. 각 장비를 순회하여 


1- 내 풀이

1) 장비의 개수만큼 순회한다.
2) 장비가 선호하는 온도의 범위를 탐색한다.
3) 장비가 선호하는 온도의 범위에 해당하는 작업량 C, G, H 를 확인한다.
4) 장비의 선호 온도 체크 1차원 배열을 만든다.
5) 장비별 범위에 해당하는 온도에 작업량을 더해준다.
5) 모든 장비 순회를 끝난 뒤 해당 온도 체크 1차원 배열에서 각 온도에 저장된 작업량 중 가장 큰 작업량을 고른다.
6) 출력한다.

'''

N, C, G, H = map(int, input().split())

temp_check = [0] * 1001

for i in range(N):
    Ta, Tb = map(int, input().split())

    for j in range(0, Ta):
        temp_check[j] += C
    
    for k in range(Ta, Tb+1):
        temp_check[k] += G
    
    for l in range(Tb+1, 1001):
        temp_check[l] += H

print(max(temp_check))