m,n = list(map(int,input().split()))

prime = [False,False]+[True for i in range(2,n+1)]

for i in range(2,int(n**(0.5))+1):
    if prime:
        for i in range(i+i,n+1,i):
            prime[i]=False

for i in range(m,n+1):
    if prime[i]:
        print(i)
