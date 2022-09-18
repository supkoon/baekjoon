a,b,c = [int(input()) for i in range(3)]


result = a*b*c

for i in range(10):
    print(str(result).count(str(i)))

