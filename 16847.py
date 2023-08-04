'''
10대 돌연변이 
to see whether a trait is really a mutation, you might have to go some generations back.

expressed traits for yourself and a number of your ancestors

A trait is a “mutant trait” if your value in that position is different from that of all your ancestors.

'''


import sys 
k = int(input())

results = []
for data in range(k):
    n,m = map(int,input().split())
    mine = list(input())
    ancestor  = []
    
    for i in range(n):
        ancestor.append(list(sys.stdin.readline()[:-1]))
    result = [0 for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mine[i]!=ancestor[j][i]:
                result[i]+=1
    
    result = [sum(list(map(lambda x : x//n,result))),m]
    results.append(result)

for idx,result in enumerate(results):
    print(f'Data Set {idx+1}:\n{result[0]}/{result[1]}')
    print()



