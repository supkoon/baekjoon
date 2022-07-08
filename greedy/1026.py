import sys
n = int(sys.stdin.readline())
A = map(int,sys.stdin.readline().split())
B = map(int,sys.stdin.readline().split())
result = 0
A=sorted(A,reverse=True)
B=sorted(B)
for i in range(n):
    result += A[i]*B[i]
sys.stdout.write(str(result))
#stack을 만들어서 pop하면서 해도 될듯