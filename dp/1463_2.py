


'''
문제
1로 만들기
세가지 연산을 사용해서 1로 만들기
1. 3으로 나누어 떨어지면 3으로 나눔
2. 2로 나누어 떨어지면 2로 나눔
3. 1을 뺌

연산을 사용하는 수의 최소값

아이디어
dp..
1에서부터 n까지 bottom up

복잡도

'''

n = int(input())
d = [0] * (n+1)

for i in range(2,n+1):
    d[i] = d[i-1]+1
    if i%3 ==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%2 ==0:
        d[i] = min(d[i],d[i//2]+1)
print(d[n])