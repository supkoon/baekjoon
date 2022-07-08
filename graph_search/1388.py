import sys
n, m = map(int,sys.stdin.readline().split())
blocks =[]

for i in range(n):
    blocks.append(list(sys.stdin.readline().rstrip()))

cnt=0
for i in range(n):
    pre =''
    for j in range(m):
        if blocks[i][j]=='-':
            if pre != blocks[i][j]:
                cnt+=1
        pre = blocks[i][j]

for i in range(m):
    pre = ''
    for j in range(n):
        if blocks[j][i] =='|':
             if pre != blocks[j][i]:
                  cnt+=1
        pre = blocks[j][i]
print(cnt)

