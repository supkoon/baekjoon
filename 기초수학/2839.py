n = int(input())
three=0
while(True):
    if n % 5 == 0:
        print(three+n//5)
        break
    n-=3
    three+=1
    if n<0:
        print(-1)
        break