count = 0
with open('data_digit.txt', 'r') as file:
    for line in file:
        count += 1

print(count)
