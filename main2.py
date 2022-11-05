import json

list_days = ['01.06.2022', '02.06.2022', '03.06.2022', '04.06.2022', '05.06.2022', '06.06.2022', '07.06.2022',
             '08.06.2022', '09.06.2022', '10.06.2022', '11.06.2022', '12.06.2022', '13.06.2022', '14.06.2022',
             '15.06.2022', '16.06.2022', '17.06.2022', '18.06.2022', '19.06.2022', '20.06.2022', '21.06.2022',
             '22.06.2022', '23.06.2022', '24.06.2022', '25.06.2022', '26.06.2022', '27.06.2022', '28.06.2022',
             '29.06.2022', '30.06.2022']

super_dict = {}
listik = {0}

for i in list_days:
    with open('data/data.txt', 'r') as file:
        count = 0
        dict_data = {}
        for line in file:
            list_ = []
            if str(i) in str(line):
                listik.add(line)


for j in listik:
    count = 0
    with open('data/data.txt', 'r') as file:
        for line in file:
            if str(j) in str(line):
                count += 1
                dict_data[j] = count
                                    # print(dict_data)

            # super_dict[i] = dict_data

for k in list_days:
    count2 = 0
    dict_2 = {}
    for key, item in dict_data.items():
        if str(k) in str(key):
            count2 += 1
            dict_2[key[10:19]] = item
    super_dict[k] = dict_2


# print(listik)
# print(super_dict)

with open("data/dict_june.json", "w", encoding='utf-8') as file:
    file.write(json.dumps(super_dict, indent=2))

