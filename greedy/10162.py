n = int(input())
a=0
b=0
c=0
while(n>=10):
    if n>=300:
        a+=1
        n-=300
    elif n>=60:
        b+=1
        n-=60
    elif n>=10:
        c+=1
        n-=10
if n==0:
    print(a,b,c)
else:
    print(-1)