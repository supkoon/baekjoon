import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().split()))
num_operators = list(map(int,sys.stdin.readline().split()))

op_map = ['+','-','*','/']
op_list=[]
for index,op in enumerate(num_operators):
    for _ in range(op):
        op_list.append(op_map[index])
num_max=-1e9
num_min =1e9

for case in permutations(op_list,n-1):
    result=num[0]
    for r in range(1,n):
        if case[r-1]=='+':
            result+=num[r]
        elif case[r-1] =='-':
            result-=num[r]
        elif case[r-1] =='*':
            result*=num[r]
        elif case[r-1] =='/':
            result = int(result/num[r])
    if result > num_max:
        num_max=result
    if result < num_min:
        num_min=result
print(num_max)
print(num_min)