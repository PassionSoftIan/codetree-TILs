'''
1. a에서 f까지의 소문자 알파벳이 주어진다.
2. +, -, * 기호도 주어진다.
3. 길이가 N인 식이 주어진다.
4. 소문자 알파벳에 해당하는 숫자를 1 ~ 4까지 배당한다.
5. 식의 결과를 최대로 한다.
6. 사칙연산은 우선순위가 없이 순서대로 간다.


'''


def calculator(depth, result):
    global max_result

    if depth == N//2+2:
        max_result = max(max_result, result)
        return

    if depth == 1:
        result = numbers[0]

    if depth >= 2:
        operation = cal[depth-2]

        if operation == '+':
            result += numbers[depth-1]

        elif operation == '-':
            result -= numbers[depth-1]

        elif operation == '*':
            result *= numbers[depth-1]

    for i in range(1, 5):
        numbers.append(i)
        calculator(depth+1, result)
        numbers.pop()

commands = list(map(str, input()))

N = len(commands)

cal = []

for i in range(1, N, 2):
    cal.append(commands[i])

numbers = []

max_result = 0

calculator(0, 0)

print(max_result)