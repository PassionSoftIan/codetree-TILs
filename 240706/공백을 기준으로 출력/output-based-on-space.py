a = input()
b = input()

c = a + b

for word in c:
    if word == ' ':
        continue
    else:
        print(word, end='')