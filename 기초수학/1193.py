import math
num = int(input())
n = math.ceil((-1+(1+8*num)**(0.5))/2)-1
i = int(num-(n)*(n+1)/2)
j = int(n-i+2)
if(n%2==1):
    print(f"{i}/{j}")
else :
    print(f"{j}/{i}")
