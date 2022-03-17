a,b = map(int,input().split())
if b<45:

    a-=1
    if a == -1:
        a = 23
    b = 60 + (b-45)
else : b-=45
print(a,b)
