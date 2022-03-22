# 0 : 48
# A : 65
# a : 97

a = input()

kapital ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = kapital.lower()
num = list('0123456789')

num_dict = {num : i for i,num in enumerate(num,48)}
kap_dict = {kapital : i for i,kapital in enumerate(list(kapital),65)}
small_dict = {small : i for i,small in enumerate(list(small),97)}

num_dict.update(kap_dict)
num_dict.update(small_dict)
print(num_dict[a])