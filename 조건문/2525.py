a, b = map(int,input().split())
c = int(input())

result = a*60 + b + c
print(result//60%24,  result%60)
