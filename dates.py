
list_of_datas = []


with open('just_datas.txt', 'r') as file:
    for line in file:
        if line.rstrip() not in list_of_datas:
            list_of_datas.append(line.rstrip())


print(list_of_datas)
