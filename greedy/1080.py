import sys
n, m = map(int,sys.stdin.readline().split())
a = []
b= []
for line in range(n):
    a.append(list(map(int,list(sys.stdin.readline().rstrip()))))
for line in range(n):
    b.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def sum_matrix(matrix):
    result = 0
    for line in matrix:
        result +=sum(line)
    return result

def flip_3x3(matrix,i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            matrix[x][y]= 1-matrix[x][y]
    return matrix
cnt=0

if (n<3 or m<3) and a!=b:
    cnt = -1
else :
    #한 번 지나간 기준점은 더 이상 바뀔 일이 없게 되며 이후 비교에 영향을 주지 않는다.
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j]!=b[i][j]:
                a=flip_3x3(a,i,j)
                cnt += 1
    if a!=b:
        cnt=-1
print(cnt)

