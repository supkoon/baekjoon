'''
문제
스네이크버드 
과일 먹으면 길이 1늘어남
지상으로부터 과일들의 높이를 줌

자신의 길이 이하만 먹을 수 있음.

처음 길이가 L일때, 최대길이는?

'''

n,l = map(int,input().split())

heights = list(map(int,input().split()))

heights.sort()
for h in heights:
    if l>=h:
        l+=1
    else:
        break
print(l)
