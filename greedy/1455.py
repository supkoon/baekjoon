n,m = map(int,input().split())

arr = []
for i in range(n):
    line = list(map(int,list(input())))
    arr.append(line)
cnt=0
for x_1 in range(n-1,-1,-1):
    for x_2 in range(m-1,-1,-1):
        if arr[x_1][x_2]:
            for x_1_ in range(x_1+1):
                for x_2_ in range(x_2+1):
                    if arr[x_1_][x_2_]:
                        arr[x_1_][x_2_]=0
                    else :
                        arr[x_1_][x_2_]=1
            cnt+=1

print(cnt)