# M N 사이의 소수
#소수 없으면 -1
m = int(input())
n = int(input())
num = list(range(m,n+1))
prime=[True for i in range(n+1)]
prime[0]=False
prime[1]=False
i=2
while i <= int(n**0.5)+1:
    for j in range(i+1,n+1):
        if j%i==0:
            prime[j]=False
    i+=1
sum_prime =0
for i in range(m,n+1):
    if prime[i] :
        sum_prime += i
if sum_prime==0:
    print(-1)
else :
    print(sum_prime)
    print(prime.index(True,m))
