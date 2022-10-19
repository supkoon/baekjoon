from collections import deque
a = input()
b = input()

result = 0

while(True):
    if len(a)==len(b):
        if a==b:
            print(1)
        else:
            print(0)
        break
    if b[-1]=='A':
        b=b[:-1]
    else:
        b=b[:-1][::-1]

