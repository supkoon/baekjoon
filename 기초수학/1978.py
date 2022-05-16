n = int(input())
num = list(map(int,input().split()))
result = 0
for i in num:
    root = int(i**(0.5))
    for j in range(2,root+1):
        if i%j ==0:
            break
        if j == root :
            result+=1

if 3 in num : result+=1
if 2 in num : result+=1
print(result)
#에라토스로 해도됨.