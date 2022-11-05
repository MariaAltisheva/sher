

listik = {0}

file = open('data/data.txt', 'r')
# with open("data.txt", "r") as file:
for line in file:
    line = line.rstrip()
    listik.add(line)
file.close()
print(listik)

aer_dict = {}

for i in listik:
    with open('data/data.txt', 'r') as file:
        count = 0
        for line in file:
            if i == line.rstrip():
                count += 1
                aer_dict[i] = count

for key, item in aer_dict.items():

    print(key, item)

