result = []
while(True):
    n = int(input())
    if n == 0 :
        break

    primes = [False,False] + [True for i in range(2,2*n+1)]
    for i in range(len(primes)):
        if primes[i] :
            for j in range(i+i,2*n+1,i):
                primes[j]=False
    result.append(sum(primes[n+1:2*n+1]))

for i in result:
    print(i)
