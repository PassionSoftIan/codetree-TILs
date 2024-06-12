ages = []

while True:
    age = int(input())

    if age < 20 or 30 <= age:
        break
    else:
        ages.append(age)

print(f'{sum(ages)/len(ages):.2f}')