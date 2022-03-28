import math
a,b,v = list(map(int,input().split()))
#마지막 움직임 v-a 에서.
day = math.ceil((v-a)/(a-b))+1
print(day)
