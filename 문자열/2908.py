a, b = input().split()
a = int(''.join(list(reversed(list(a)))))
b = int(''.join(list(reversed(list(b)))))
print(a if a>b else b)