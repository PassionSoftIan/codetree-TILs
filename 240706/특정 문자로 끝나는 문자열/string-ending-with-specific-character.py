words = []

for i in range(10):
    words.append(input())

key = input()

bit = 0
for word in words:
    if word[-1] == key:
        print(word)
        bit = 1

if bit == 0:
    print('None')