'''
1. N명의 학생에게 B만큼의 예산으로 선물을 산다.
2. 학생마다 원하는 선물 가격, 배송비가 있다.
3. 선물 하나를 정해 반값으로 할인받을 수 있다.
4. 선물 가능한 학생의 최대 숫자를 구하라.

1- 내 풀이

1) 학생 수 만큼 순회를 한다.
2) 학생 한 명을 특정하여 학생이 원하는 선물 가격을 반 값으로 할인한 뒤 배송비를 더한다.
3) 나머지 학생을 원활하게 구하기 위해 학생이 원하는 가격과 배송비를 합친 뒤 학생의 번호와 함께 넣어
2차원 배열을 만든다.
4) 2차원 배열을 가격 기준으로 오름차순으로 정렬한다.
5) 순서대로 가격을 더해주다가 예산을 초과하면 그만한 뒤 학생 수를 현재 최대 학생 수와 비교한다.
6) 더 높은 숫자를 최대 학생 수로 교체한다.
7) 최대 학생수를 출력한다.

'''

N, B = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(N)]

costs = []

costs.sort(key=lambda x : x[1])

for i in range(N):
    gift, delevery = students[i][0], students[i][1]
    costs.append([i, gift+delevery])

max_result = 0
for i in range(N):
    count = 0
    temp_cost = 0
    discounted = (students[i][0] // 2) + students[i][1]
    if discounted <= B:
        count += 1
    else:
        continue

    for j in range(N):
        if i == costs[j][0]:
            continue
        
        if temp_cost + costs[j][1] <= B:
            temp_cost += costs[j][1]
            count += 1
        else:
            break

    max_result = max(max_result, count)

print(max_result)