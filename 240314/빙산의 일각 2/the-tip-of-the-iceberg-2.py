'''
1. 해수면의 높이에 따라 물에 잠기는 빙산이 있음.
2. 빙산의 개수 N이 주어짐.
3. N개의 빙산들의 높이가 주이점.
4. 빙산들이 물에 잠기지 않아야함.
5. 빙산이 연결되어있는 경우 한 덩어리
5. 해수면 높이 설정.
6. 가능한 빙산 덩어리 최대 개수를 구하라.

1- 내 풀이

1) 빙산을 나타낼 1차원 배열 생성
2) for i in range(빙산의 최대 높이) 순회 하며 해수면 높이 설정
3) 해수면 높이를 설정하고 빙산 배열을 돌며 -= 1
4) 빙산 배열을 다시 순회하며 0이 나올 때는 덩어리가 끝난 것으로 가정 count += 1
5) 해수면 높이가 바뀌기 전 max_result와 count를 비교하여 더 큰 것으로 max_result 교체
6) max_result 출력

'''

N = int(input())

ice_berg = [0] * 100

for i in range(N):
    ice_berg[i] = int(input())

max_hegith = max(ice_berg)

max_result = 0
for i in range(max_hegith):
    temp_ice_berg = [ ice_berg[_] for _ in range(N)]

    for j in range(N):
        if temp_ice_berg[j] - i < 0:
            temp_ice_berg[j] = 0
        else:
            temp_ice_berg[j] -= i
    
    count = 0
    bit = 0
    for check in range(N):

        if temp_ice_berg[check] != 0:
            bit = 1

        if bit == 1 and temp_ice_berg[check] == 0:
            bit = 0
            count += 1
            
        if bit == 1 and check == N-1:
            count += 1

print(max_result)