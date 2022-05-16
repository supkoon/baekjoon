a, b = map(int,input().split())
def gcd(a,b):
    while(True):
        if b>a:
            b,a = a,b
        if a%b==0 : return b
        else : a%=b
def lcm(a,b):
    return(a*b//gcd(a,b))
print(gcd(a,b))
print(lcm(a,b))
