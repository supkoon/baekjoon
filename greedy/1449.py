from collections import deque
n , l = map(int,input().split())
points = sorted(list(map(int,input().split())))
points=deque(points)
cnt=0
while(points):
    tape = points.popleft()-0.5+l
    cnt+=1
    while(points):
        if points[0]+0.5<=tape:
            points.popleft()
        else:
            break
print(cnt)