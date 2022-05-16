n = int(input())
answer =False
for i in range(n):
    result = i + sum(map(int,list(str(i))))
    if result == n:
        print(i)
        answer = True
        break
if not answer:
    print(0)