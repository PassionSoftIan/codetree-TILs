'''
1. N 명의 사람들
2. 일직선에 주어진 번호에 서있음.
3. G, H 중 알파벳 할당.
4. 사진의 크기 K
5. G는 1점 H는 2점
6. 최대 점수 구하라.

'''

N, K = map(int, input().split())

arr = [0] * 10001

start =10001
end = 0

for i in range(N):
    location, alphabet = map(str, input().split())
    location = int(location)

    start = min(start, location)
    end = max(end, location)

    if alphabet == 'G':
        arr[location] = 1
    
    else:
        arr[location] = 2

max_count = 0
for i in range(start, end - K):
    count = 0
    for j in range(K+1):
        count += arr[i + j]
    
    max_count = max(max_count, count)

print(max_count)