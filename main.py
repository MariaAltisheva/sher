

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








#
# result = 0
# AER = 0
# ABA = 0
# ARH = 0
# GRV = 0
#
# file = open('data.txt', 'r')
# # with open("data.txt", "r") as file:
# for line in file:
#     if 'ABA' in line:
#         ABA += 1
#     if 'AER' in line:
#         AER += 1
#     if 'ARH' in line:
#         ARH += 1
#     if 'GRV' in line:
#         GRV += 1
#     result += 1
# file.close()
#
# print(result)
# print("AER =", AER)
# print("ABA =", ABA)
# print("ARH =", ARH)
# print("GRV =", GRV)
