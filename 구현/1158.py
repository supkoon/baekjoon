'''
문제
요세푸스 문제
N명이 원으로 앉아있음. 
순서대로 k번째 제거
계속 제거
N명이 제거될때까지 함.

ex. 7,3 요세푸스 순열
1~7번이
계속 3번째 제거 

3 --> 6 --> 2 --> 7 

아아디어
계속 n번째 사람이 사라짐. 
포인터를 계속 가지고 있으면서 
다음 사람은 (point+3)%n을 제거. 

pop(3)

복잡도

변수
'''

n,k = map(int,input().split())
a = list(range(1,n+1))
s = 0
print('<',end='')
while(a):
    s = (s-1+k)%len(a)
    if len(a)>1:
        print(a.pop(s),end=', ')
    else:
        print(a.pop(s),end='>')
        

#1 2 0 4 5 6 7
#1 2 0 4 5 0 7
#1 0 0 4 5 0 7
#1 2 0 4 5 0 7