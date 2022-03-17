a,b,c = map(int,input().split())
if (a==b==c):
    print(10000+a*1000)

elif (a==b) |(a==c):
    print(1000+a*100)
elif (b==c):
    print(1000+b*100)

else:
    print(sorted([a,b,c],reverse=True)[0]*100)



#먼저 정렬해서 가운데 인덱스로 할수도 있음.