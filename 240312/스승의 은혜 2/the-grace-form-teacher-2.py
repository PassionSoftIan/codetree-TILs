'''
1- 내 풀이

0) 원하는 금액이 적은 순서로 정렬.
1) 학생 한 명을 골라서 반값으로 할인하기.
2-1) 반값으로 할인받은 금액이 예산보다 적거나 같으면 학생수를 한 명올리고 구매비용에 할인 값 더한 뒤 진행
2-2) 클 경우 다음 학생 진행
3) 학생들 차례로 선물 가격을 현재 구매비용에 더하여 예산을 초과하는지 확인
4-1) 초과 하지 않을 경우 학생 수 더하기
4-2) 초과하는 경우 이전 학생 까지의 기록만 저장
5) 학생 수를 체크하여 최대 값 갱신
5) 최대 학생수 출력
'''

N, B = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr.sort()

max_result = 0
for i in range(N):
    discounted = arr[i]//2
    
    student_count = 0

    if discounted <= B:
        student_count += 1
    else:
        continue

    cost = discounted
    for j in range(N):
        if i == j:
            continue

        if cost + arr[j] <= B:
            student_count += 1
            cost += arr[j]
        else:
            break
    
    max_result = max(max_result, student_count)

print(max_result)