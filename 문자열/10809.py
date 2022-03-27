result = [-1 for i in range(26)]
alpha_index = {alpha:index for index,alpha in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}

a = list(input().upper())

for index,i in enumerate(a):
    if (i in alpha_index.keys()) & (result[alpha_index[i]]==-1):
        result[alpha_index[i]]=index
for i in result:
    print(i,end=' ')