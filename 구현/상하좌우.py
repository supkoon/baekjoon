'''
풀이
1,1
    ... 
        N,N

시간복잡도
O(N)

변수
n : 크기
moves : 지도,list
'''



# mapping = [[1,0],[-1,0],[0,1],[0,-1]]
mapping = {'R':[0,1], 'U':[-1,0],'D':[1,0],'L':[0,-1]}

n = int(input())
moves = input().split()
moves = list(map(lambda x : mapping[x],moves))

curr = [1,1]
for move in moves:
    dx = move[0]
    dy = move[1]
    x = curr[0]+dx
    y = curr[1]+dy
    if 0<x<<n and 0<y<n:
        curr[0] = x
        curr[1] = y 
    else :
        continue
    
print(curr[0],curr[1])



