import sys
a = sys.stdin.readline().rstrip()
if len(a)==1:
    a+='0'
num = 0
result = a
while(True):
    num+=1
    result = result[-1] + str(int(result[0])+int(result[-1]))[-1]
    if a == result:
        print(num)
        break

