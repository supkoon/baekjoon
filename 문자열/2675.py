import sys
a = int(input())
result_ = []
for i in range(a):
    a,b = sys.stdin.readline().split()
    a = int(a)
    result = ''
    for i in b:
        result+=a*i
    result_.append(result)

for i in result_:
    print(i)


