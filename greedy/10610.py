'''
문제
숫자를 받아서
가장 큰 30의 배수로 만들기
못만들면 -1 

아이디어
10^5개의 숫자까지 가능함

30 60 90 120 150 180 210 

1.0이 무조건 있어야함.

2. 
030
060
090
120
150
180
210
240
270
300
330
360
990
1020
1050
1060
자리수 합이 3인듯

복잡도

'''
n = list(input())
n = sorted(n,reverse=True)
n = list(map(int,n))

try : 
    idx = n.index(0)
    if sum(n)%3==0:
        for i in n:
            print(i,end='')
    else:
        print(-1)
except:
    print(-1)