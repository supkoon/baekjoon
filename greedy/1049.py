m,n = map(int,input().split())
pack_6 = list()
pack_1 = list()

for i in range(n):
    a,b = map(int,input().split())
    pack_6.append(a)
    pack_1.append(b)

price_6= min(pack_6)
price_1= min(pack_1)


if m < 6:
    if price_6<price_1*m:
        print(price_6)
    else:
        print(price_1*m)
else:
    if price_6<price_1*6:
        if m%6*price_1<price_6:

            print(m//6*price_6+m%6*price_1)
        else:
            print((m//6+1)*price_6)
    else:
        print(price_1*m)





