goal = int(input())
n_mal = int(input()) #키셋팅
if n_mal:
    keys = input().split()
else:
    keys=[]
min_moves=abs(100-goal)
flag=False
for i in range(1000001):
    for j in str(i):
        if j in keys:
            flag=True
            break
    if not flag:
            min_moves = min(min_moves,len(str(i))+abs(i-goal))
    flag=False
print(min_moves)
