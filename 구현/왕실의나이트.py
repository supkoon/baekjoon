
'''
아이디어
dx,dy를 통해 나이트가 갈 수 있는 경우 완전탐색

복잡도
O(1)

변수 
dx,dy
x,y 
cnt 
'''
x,y = input()
y = int(y)
x = ord(x)-96

tmp = x
x = y
y = tmp 

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]
cnt=0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1<=nx<=8 and 1<=ny<=8:
        cnt+=1

print(cnt)