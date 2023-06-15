import sys
colors = []
for i in range(5):
    c,n = sys.stdin.readline().split()
    n = int(n)
    if c =='R':
        colors.append(n)
    elif c =='B':
        colors.append(10+n)
    elif c =='Y':
        colors.append(20+n)
    else :
        colors.append(30+n)
print(colors)
colors.sort()
result = 0
for i in colors:
    pass
