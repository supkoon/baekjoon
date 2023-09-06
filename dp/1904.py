'''
01타일

01 타일 2진수열

1, 00 있음

길이 N이 주어질때 지원이가 만들 수 있는 모든 경우의 수 구하기

경우의수 구해서 15746으로 나눈 나머지 .

100만이고, 0.75니깐 일반적 방법으론 안됨. O(N)

--> dp 


'''

def solution(n):

    if n==1:
        return 1 
    elif n== 2:
        return 2
    else:
        d2 = 1
        d1 = 2
        cur = 0 
        for i in range(3,n+1):
            cur = (d1+d2)%15746
            d1,d2 = cur,d1
        
        return cur

n  = int(input())
print(solution(n))

# 결과 값에만 나눠주는 게 아니라 반복문 안에서도 수시로 나머지 연산을 해 주어야 메모리 초과가 발생하지 않는다. (값이 int값을 초과하기 때문에 n = 1000000 일 경우 엄청나게 많은 메모리를 차지하게 된다.)

