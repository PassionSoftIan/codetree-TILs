'''
1. 독서실 이용자들의 좌석이 주어진다.
2. 한 명을 추가하여 배치한다.
3. 가장 가까운 거리의 사람 사이 거리가 최소가 되게하라.


1- 내 풀이

1) 두 사람의 거리가 가장 먼 곳 중앙에 배치한다.
2) 배치한 뒤 가장 가까운 사람간 거리를 구한다.
3) 출력한다.

'''

N = int(input())

seat = list(map(int, input()))

count = 0
start = 0
end = 0
for i in range(N):
    if seat[i] == 0:
        continue

    temp_count = 0
    for j in range(i+1, N):
        if seat[j] == 1:
            temp_count += 1
            if count < temp_count:
                start = i
                end = j
                count = temp_count
            break
        else:    
            temp_count += 1

seat[(start + end)//2] = 1

min_dist = 1001
temp_dist = 0
for i in range(1, N):
    temp_dist += 1
    if seat[i] == 1:
        if min_dist > temp_dist:
            min_dist = temp_dist
        temp_dist = 0

print(min_dist)