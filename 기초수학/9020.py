import sys
n = int(sys.stdin.readline())
result = []
for case in range(n):
    num = int(sys.stdin.readline())
    primes = [False,False]+[True for i in range(2,num+1)]
    for i in range(2,int(num**(0.5))+1):
        if primes[i]:
            for i in range(i*2,num+1,i):
                primes[i]=False
    middle = len(primes)//2
    for i in range(middle,num+1):
        if primes[i]:
            if primes[num-i]:
                result.append([num-i,i])
                break
for i,j in result:
    print(i,j)
