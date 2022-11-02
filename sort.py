import json

list_for_key = ["5N_OVB", "FV_AER", "N4_AER", "N4_CEK", "N4_KEJ", "N4_KZN", "N4_LED", "N4_MRV", "N4_OSW", "N4_SVX", "SU_ABA", "SU_AER", "SU_ARH", "SU_ASF", "SU_CEK", "SU_GRV", "SU_HMA", "SU_IGT", "SU_IJK", "SU_IKT", "SU_KGD", "SU_KHV", "SU_KJA", "SU_KUF", "SU_KZN", "SU_LED", "SU_MCX", "SU_MMK", "SU_MQF", "SU_MRV", "SU_NJC", "SU_NUX", "SU_OSW", "SU_OVB", "SU_PEE", "SU_PKC", "SU_REN", "SU_SCW", "SU_SGC", "SU_STW", "SU_SVX", "SU_TJM", "SU_RGK", "SU_UUS", "SU_UFA", "SU_YKS", "SU_VOG", "SU_VVO", "EU_AYT", "SU_AYT", "SU_IST", "SU_MSQ", "SU_OSS", "SU_FRU", "XC_AYT", "JU_BEG", "6Q_DAM", "FG_KBL", "FG_MZR", "N4_IKA", "W5-IKA"]

list_for_sort = [9.26717671767177, 1.58828382838284, 0.00937593759375938, 0.337533753375338, 0.230648064806481, 0.0825082508250825, 0.00562556255625563, 0.00375037503750375, 3.15031503150315, 1.15699069906991, 2.52962796279628, 5.13613861386139, 0.0543804380438044, 0.00562556255625563, 0.00375037503750375, 0.255025502550255, 6.19749474947495, 0.00187518751875188, 0.0168766876687669, 4.89611461146115, 0.165016501650165, 0.0131263126312631, 6.18624362436244, 0.0281278127812781, 0.0243774377437744, 4.96362136213621, 0.0281278127812781, 0.0543804380438044, 6.26500150015002, 0.0487548754875488, 1.48702370237024, 3.41284128412841, 0.416291629162916, 6.48627362736274, 0.0637563756375638, 0.0187518751875188, 3.43159315931593, 0.0487548754875488, 4.76110111011101, 0.0375037503750375, 2.46587158715872, 2.79590459045905, 0.603810381038104, 0.00187518751875188, 0.116261626162616, 0.260651065106511, 0.00937593759375938, 0.00562556255625563, 7.06383138313831, 1.18324332433243, 0.0112511251125113, 0.03000300030003, 5.04425442544254, 2.54275427542754, 0.24002400240024, 3.72224722472247, 0.504425442544255, 0.196894689468947, 0.110636063606361, 0.174392439243924, 0.0468796879687969]

dict_f = dict(zip(list_for_key, list_for_sort))

#print(dict_f)

sorted_values = sorted(dict_f.values())
#print((sorted_values))

sorted_dict = {}

for i in sorted_values:
    for k in dict_f.keys():
        if dict_f[k] == i:
            sorted_dict[k] = dict_f[k]
print(sorted_dict)

with open("data/dict_sort.json", "w", encoding='utf-8') as file:
    file.write(json.dumps(sorted_dict, indent=2))
