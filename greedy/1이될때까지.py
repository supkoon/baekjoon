# n,k를받음.
#다음 두가지 행동이 가능 
# n을 k로 나눈다, n에서 1을 뺀다.
# 1까지 가는 가장 적은 횟수의 연산 수


#방법
#무한 반복문
#k로 나누어 떨어지는 가장 가까운 정수 tgt를 찾고, 그 차이만큼 cnt += 함. 
#tgt를 k로 나누기 cnt +=1

#변수
#n,k, tgt, cnt  


n, k = map(int,input().split())
cnt = 0
while(True):

    tgt = (n//k)*k 
    cnt += (n-tgt)
   
    n = tgt 
    if n<k:
        break
    
    n/=k
    cnt+=1

cnt += (n-1)

print(cnt)



