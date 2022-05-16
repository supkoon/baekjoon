import sys
n = int(sys.stdin.readline())
result = []
for case in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        result.pop()
    else :
        result.append(num)

sys.stdout.write(str(sum(result)))
