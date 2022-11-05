import json

list_days = ['6/1/2022', '6/12/2022', '6/28/2022', '6/23/2022', '6/30/2022', '6/26/2022', '6/21/2022', '6/14/2022',
             '6/3/2022', '6/11/2022', '6/17/2022', '6/6/2022', '6/26/2022', '6/22/2022', '6/9/2022', '6/24/2022',
             '6/10/2022', '6/27/2022', '6/19/2022', '6/31/2022', '6/6/2022', '6/18/2022', '6/13/2022', '6/4/2022',
             '6/2/2022', '6/16/2022', '6/29/2022', '6/7/2022', '6/20/2022', '6/16/2022', '6/8/2022']

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
            dict_2[key[9:16]] = item
    super_dict[k] = dict_2


# print(listik)
print(super_dict)

with open("data/dict_june.json", "w", encoding='utf-8') as file:
    file.write(json.dumps(super_dict, indent=2))

