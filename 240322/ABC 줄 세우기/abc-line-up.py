'''
1. N명의 사람이 있다.
2. 서있는 순서가 A부터 순서대로 알파벳 형태로 주어진다.
3. 알파벳 순서로 줄을 세우고자 한다.
4. 단, 순서대로 줄을 세우기 위해서는 '인접한 두 사람의 위치를 바꾸는 행위만' 가능하다.
5. 자리를 바꾸는 최소 횟수를 구하라.


1 - 내 풀이

1) while 문을 돌면서 for i in range(N-1)동안 people[i] 보다 people[i+1]이 더 작으면 위치를 바꾼다.
2) 위치를 바꿀 때 마다 min_count += 1을 한다.
3) min_count를 출력한다.

'''

N = int(input())

people = list(map(lambda x: ord(x) - 65, input().split()))

min_count = 0

bit = 0
while bit == 0:
    bit = 1
    for i in range(N-1):
        if people[i] > people[i+1]:
            people[i], people[i+1] = people[i+1], people[i]
            min_count += 1
    
    for i in range(N):
        if i != people[i]:
            bit = 0
            break

print(min_count)