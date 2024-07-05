words = []

for i in range(10):
    words.append(input())

key = input()

for word in words:
    if word[-1] == key:
        print(word)