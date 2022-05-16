import sys
n = map(int,list(sys.stdin.readline().rstrip()))
for i in sorted(n,key = lambda x : -x):
    sys.stdout.write(str(i))
