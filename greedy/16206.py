n,m = map(int,input().split())

cakes = list(map(int,input().split()))
cakes.sort(key=lambda x:(x%10,x))
cake_cnt = 0
for i in range(n):
    cnt = cakes[i]//10
    if  cakes[i]%10 ==0 :
        if cnt-1<=m:
            cake_cnt+=cnt
            m-= cnt-1
        else:
            cake_cnt+=m
            m-=m
    else:
        if cnt <=m:
            cake_cnt +=cnt
            m-=cnt
        else:
            cake_cnt+=m
            m-=m
print(cake_cnt)
