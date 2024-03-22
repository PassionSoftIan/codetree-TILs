'''
1. N명의 사람이 있다.
2. 서있는 순서가 A부터 순서대로 알파벳 형태로 주어진다.
3. 알파벳 순서로 줄을 세우고자 한다.
4. 단, 순서대로 줄을 세우기 위해서는 인접한 두 사람의 위치를 바꾸는 행위만 가능하다.
5. 자리를 바꾸는 최소 횟수를 구하라.



'''

N = int(input())

people = list(map(lambda x: ord(x) - 65, input().split()))

min_count = 0
for i in range(N):
    if i == people[i]:
        continue
    for j in range(N):
        if i == people[j]:
            people[j] = people[i]
            people[i] = i
            min_count += 1

print(min_count)