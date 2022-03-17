import sys
a,b = map(int,sys.stdin.readline().split())

string = list(sys.stdin.readline().split())

result = [i for i in string if int(i) < b]
# for i in result:
#     print(i,end= ' ')

print(' '.join(result))