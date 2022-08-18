# arr = input().split('-')
# result=0
# for i in arr[0].split('+'):
#     result+=int(i)
# for i in arr[1:]:
#     for j in i.split('+'):
#         result-=int(j)
# print(result)

import re
a = input()
p = re.compile("[0-9]+|\W")
a = p.findall(a)
print(a)
global_min=10**6
if len(a)==1:
    print(int(a[0]))
elif len(a)==0:
    print(0)
else:
    for i in range(len(a)):
        if i%2==1: continue
        for j in range(i+2,len(a),2):
            result=eval(''.join(a[:i]+[str(eval(''.join(map(int,a[i:j+1]))))]+a[j+1:]))
            if result<global_min:
                global_min=result
    print(global_min)


