'''
문제
에라토스테네스의 체

아이디어
에라토스테네스의 체는, 앞에서부터 배수를 지워나가는 방법.
개선할 수 있는 여지는 n**0.5 +1 까지만 시도해 보는것.

k번째로 지워진 숫자는 어떻게 찾지..?
에라토스테네스 순서니간 그냥 앞에서부터 카운트하자. 



복잡도
O(n^2)


'''


n,k = map(int,input().split())
#k는 k번째로 지워진 숫자

prime = [False,False] + [True for _ in range(2,n+1)]
cnt = 0 
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if prime[j]:
            cnt+=1
            prime[j]=False

            if cnt == k:
                print(j)
                exit()


