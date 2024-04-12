income = int(input())
count = 0
total = income

while income != 0:
    income = int(input())
    count += 1
    total += income

print(total/count)
