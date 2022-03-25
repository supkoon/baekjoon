
a = input().lower()
alpha = list('abcdefghijklmnopqrstuvwxyz')
croa_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croa_list.extend(alpha)

for i in croa_list:
    if a.find(i) !=-1:
        a = a.replace(i,'0')
print(len(a))