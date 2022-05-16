import sys
x,y,w,h = list(map(int,sys.stdin.readline().split()))
result = min([x,w-x,y,h-y])
print(result)