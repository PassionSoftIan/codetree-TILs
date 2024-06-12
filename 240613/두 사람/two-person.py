p1_age, p1_gender = input().split()

p2_age, p2_gender = input().split()

result_1 = int(p1_age) >= 19 and p1_gender == 'M'
result_2 = int(p2_age) >= 19 and p2_gender == 'M'

if result_1 == 1 or result_2 == 1:
    print(1)

else:
    print(0)