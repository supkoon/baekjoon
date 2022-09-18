import sys

a = []
for line in sys.stdin:
    try :    a.append(int(line))
    except : break
a_max = max(a)
print(a_max,a.index(a_max)+1,sep = '\n')



'''
[int(input()) for i in range(9)]
'''
