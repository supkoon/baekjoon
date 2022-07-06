n = int(input())
dn = [0]*91
def fibo(n):
    if n==1 or n==2 :
        return 1
    if dn[n]!=0:
        return dn[n]
    dn[n] = fibo(n-1)+fibo(n-2)

    return dn[n]
print(fibo(n))