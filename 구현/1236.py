n, m = map(int,input().split())
x_1 = [False]*n #세로
x_2 = [False]*m #가로

for i in range(n):
  line = list(input())
  for idx,j in enumerate(line):
    if j=='X':
      x_1[i]=True
      x_2[idx]=True
cnt = x_1.count(False)+x_2.count(False)-min(x_1.count(False),x_2.count(False))
print(cnt)