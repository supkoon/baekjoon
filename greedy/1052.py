n,k = map(int,input().split())

cnt =0

while(bin(n)[::-1].count('1')>k):
    idx = bin(n)[::-1].index('1')
    cnt+=2**idx
    n+=2**idx

print(cnt)