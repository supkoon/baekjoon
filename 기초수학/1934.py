# # def gcd(a,b):
# #     while(True):
# #         if b>a:
# #             b,a = a,b
# #         if a%b==0: return b
# #         else : a%=b
# # def lcm(a,b):
# #     return (a*b//gcd(a,b))
# # n = int(input())
# # for case in range(n):
# #     a, b = map(int,input().split())
# #     print(lcm(a,b))
import sys
t = int(sys.stdin.readline())

def gcd(a,b):
    if b==0 : return a
    return gcd(b,a%b)

while t:
    a, b = map(int,sys.stdin.readline().split())
    print(a*b//gcd(a,b),gcd(a,b))

    t-=1

