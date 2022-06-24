a , b = map(list,input().split())
if len(b)>len(a):
    print(0)
else :
    cnt = 0
    for i in range(len(a)):
        if a[i]==b[i]:
            if a[i]=='8':
                cnt+=1
        else:
            break
    print(cnt)
