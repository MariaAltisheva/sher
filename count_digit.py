total = 0
with open('data_digit.txt', 'r') as file:
    for line in file:
        if 'TotalSumm' in line:
            continue
        else:
            total += float(line.rstrip())

print(round(total))
