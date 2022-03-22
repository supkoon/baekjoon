import sys
a = int(input)

for i in range(a):
    a,b = sys.stdin.readline().split()
    a = int(a)
    result = ''
    for i in b:
        result+=a*i

print(result)


