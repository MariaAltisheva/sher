total = 0
with open('data_digit.txt', 'r') as file:
    for line in file:
        total += float(line.rstrip())

print(total)
