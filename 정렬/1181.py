import sys
n = int(sys.stdin.readline())
result = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in result:
        result.append(word)

for _ in sorted(result, key = lambda x : (len(x),x)):
    sys.stdout.write(_+"\n")