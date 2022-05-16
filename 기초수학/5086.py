result=[]
while(True):
    a ,b = map(int,input().split())
    if (a+b==0):
        break
    if a>b:
        if(a%b)==0:
            result.append('multiple')
        else: result.append('neither')
    else :
        if(b%a)==0:
            result.append('factor')
        else: result.append('neither')

for i in result:
    print(i)