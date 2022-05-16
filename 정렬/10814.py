import sys
n = int(sys.stdin.readline())
result = []
for index,_ in enumerate(range(n)):
    age, name = sys.stdin.readline().split()
    result.append([int(age),name,index])

for i in sorted(result,key = lambda x: (x[0],x[2])):
    sys.stdout.write(str(i[0])+" ")
    sys.stdout.write(i[1]+"\n")


