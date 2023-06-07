'''
아이디어
n이 3의 배수일때
3600개

n이 3이 포함 될때
    분이 3이 포함될때 
        03~53 : 6개 
        31~39 : 9개 총 15개 
    분이 3이 포함 안될때    
        45개     
    19 개
        

복잡도
o(n)

변수
n : 시
cnt : 3의 수
'''
import time

t1 = time.time()
n = int(input())
cnt = 0 

for i in range(n+1):
    if i//10==3 or i%10==3:
        cnt += 3600 
    else : 
        #분에 따라. 
        cnt += 15 * 60 +  45 * 15


'''
brute force 완전탐색 풀이
'''

print(cnt)
t2 = time.time()
print(t2-t1)


t1 = time.time()
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)

t2 = time.time()
print(t2-t1)

