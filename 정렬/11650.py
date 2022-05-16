import sys
n = int(sys.stdin.readline())
result = []

for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    result.append([x,y])

for x,y in sorted(result,key = lambda x : (x[0],x[1])):
    sys.stdout.write(str(x)+ " ")
    sys.stdout.write(str(y)+"\n")

