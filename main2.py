import json

list_days = ['5/1/2022', '5/12/2022', '5/28/2022', '5/23/2022', '5/30/2022', '5/25/2022', '5/21/2022', '5/14/2022',
             '5/3/2022', '5/11/2022', '5/17/2022', '5/5/2022', '5/26/2022', '5/22/2022', '5/9/2022', '5/24/2022',
             '5/10/2022', '5/27/2022', '5/19/2022', '5/31/2022', '5/6/2022', '5/18/2022', '5/13/2022', '5/4/2022',
             '5/2/2022', '5/15/2022', '5/29/2022', '5/7/2022', '5/20/2022', '5/16/2022', '5/8/2022']

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

with open("data/dict_c.json", "w", encoding='utf-8') as file:
    file.write(json.dumps(super_dict, indent=2))

