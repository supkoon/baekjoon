import math
T = int(input())
#combination 활용
for case in range(T):
    n,m = map(int,input().split())
    print(math.comb(m,n))


