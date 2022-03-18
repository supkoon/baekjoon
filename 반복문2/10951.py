import sys
result = []
while(True):
    try:
        a, b = map(int,sys.stdin.readline().split())
        result.append(a+b)

    except:
        break

for i in result:
    print(i)