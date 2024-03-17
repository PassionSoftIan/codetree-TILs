'''
1. 보석방에 N개의 보석 존재.
2. 가방의 수용 가능 무게 M.
3. 가방의 수용 가능 무게만큼 들고 나올 수 있음.
4. 보석은 종류별로 단 한개.
5. 쪼개서 담는 것 가능.
6. 최대 가치를 구하라.

1- 내 풀이

1) 최대 가치를 저장할 max_result 생성
2) 쪼개기가 가능하기 때문에 꽉 채우면 됨.(DP가 아닌 Greedy로 가능)
3) 보석의 무게대비 가치를 저장할 배열 만들기. value_table = [0] * N
4) for i in range(N)을 순회하며 value_table[i] = jewelry[i][1] / jewelry[i][0] 가치 저장.
5) 가치를 value_table.sort() 정렬
6) for i in range(N-1, -1, -1) 순회하며 뒤에서 부터 담기 시작.
7) 지금 가방에 담긴 것을 나타낼 now_M = 0 생성.
8) if M - now_M > jewelry[i][0]일 경우 now_M += jewelry[i][0] 무게 더해주고, max_result += jewelry[i][1]
9) else max_result += ((jewelry[i][0] / M - now_M) * (value_table[i]))
10) max_result 출력

'''

# N 보석의 개수, M 가방의 크기
N, M = map(int, input().split())

# w 보석의 무게, v 보석의 가치
jewelry = [list(map(int, input().split())) for _ in range(N)]

value_table = [[0] * 2 for _ in range(N)]

for i in range(N):
    value_table[i][1] = jewelry[i][1] / jewelry[i][0]
    value_table[i][0] = i

value_table.sort(key=lambda x : x[1], reverse=True)

max_result = 0

now_M = 0
for i in range(N):
    idx = value_table[i][0]
    if M - now_M > jewelry[idx][0]:
        now_M += jewelry[idx][0]
        max_result += jewelry[idx][1]
    else:
        max_result += ((M - now_M) * value_table[i][1])
        break
    
print(format(round(max_result, 3), '.3f'))