import sys
result = [ ]
while(True):
    a, b = map(int,sys.stdin.readline().split())
    if (a==b==0):
        break
    result.append(a+b)
for i in result :
    print(i)

    