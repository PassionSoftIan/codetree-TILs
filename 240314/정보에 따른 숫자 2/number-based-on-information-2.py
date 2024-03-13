'''
1. 1차 수직선에 T개의 S, N이 존재.
2. k로부터 가장 가까이 있는 S까지 거리 d1
3. k로부터 가장 가까이 있는 N까지 거리 d2
4. d1 <= d2인 경우 k는 특별한 위치
5. range(a, b+1) 위치 를 체크하여 특별한 위치 개수를 구하라.

T = S, N의 개수 총 합
a = 시작 점
b = 끝 점

1- 내 풀이

1) 1001칸의 1차원 배열을 만든다.
2) 1차원 배열에 S와 N을 배치한다.
3) for i in range(a, b+1)를 순회한다.
4) i를 1차원 배열의 Index로 잡고 왼쪽 오른쪽을 탐색하여 S를 찾는다.
5) 둘 중 더 가까운 쪽의 거리를 d1으로 잡는다.
6) N도 마찬가지로 진행하여 d2를 잡는다.
7) d1 <= d2인지 확인한다.
8) 맞다면 result += 1을 한다.
9) result를 출력한다.

'''


def S_search(check_point):

    S_dist_left = 0
    left = check_point
    while arr[left] != 'S':
        S_dist_left += 1
        left -= 1

        if left < 0:
            S_dist_left = 1001
            break

    S_dist_right = 0 
    right = check_point
    while arr[right] != 'S':
        S_dist_right += 1
        right += 1

        if right > b:
            S_dist_right = 1001
            break
    
    if S_dist_left < S_dist_right:
        return S_dist_left
    
    return S_dist_right


def N_search(check_point):

    N_dist_left = 0
    left = check_point
    while arr[left] != 'N':
        N_dist_left += 1
        left -= 1

        if left < 0:
            N_dist_left = 1001
            break

    N_dist_right = 0 
    right = check_point
    while arr[right] != 'N':
        N_dist_right += 1
        right += 1

        if right > b:
            N_dist_right = 1001
            break
    
    if N_dist_left < N_dist_right:
        return N_dist_left
    
    return N_dist_right


T, a, b = map(int, input().split())

arr = [0] * 1001

for i in range(T):
    point, idx = map(str, input().split())

    idx = int(idx)

    arr[idx] = point

result = 0
for i in range(a, b+1):
    d1 = S_search(i)
    d2 = N_search(i)

    if d1 <= d2:
        result += 1

print(result)