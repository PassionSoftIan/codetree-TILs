'''
1. a에서 f까지의 소문자 알파벳이 주어진다.
2. +, -, * 기호도 주어진다.
3. 길이가 N인 식이 주어진다.
4. 소문자 알파벳에 해당하는 숫자를 1 ~ 4까지 배당한다.
5. 식의 결과를 최대로 한다.
6. 사칙연산은 우선순위가 없이 순서대로 간다.


'''


def calculator(depth):
    global max_result

    if depth == 7:
        result = numbers[alphabet[commands[0]]]
        for command in range(1, N):
            if commands[command] in cal:
                operator = commands[command]

                if operator == '+':
                    result += numbers[alphabet[commands[command+1]]]

                if operator == '-':
                    result -= numbers[alphabet[commands[command+1]]]

                if operator == '*':
                    result *= numbers[alphabet[commands[command+1]]]
        
        max_result = max(max_result, result)
        return
        

    for i in range(1, 5):
        numbers.append(i)
        calculator(depth+1)
        numbers.pop()

commands = list(map(str, input()))

N = len(commands)

alphabet = {
    'a': 0,
    'b': 1, 
    'c': 2, 
    'd': 3, 
    'e': 4, 
    'f': 5
    }

cal = ['+', '-', '*']

numbers = []

max_result = 0

calculator(0)

print(max_result)