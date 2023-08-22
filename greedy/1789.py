'''
문제
수들의 합 
서로 다른 N개의 자연수의 합 S
N의 최댓값은?



아이디어
작은것부터 더해?

200 199,1 198,2 197,1,2

196 1,2,


1
1,2
1,2,3



'''

n = int(input())

result = 0
cnt = 0 
for i in range(1,n+1):
    if result+i > n:
        break
    result+=i
    cnt+=1
print(cnt)
    

