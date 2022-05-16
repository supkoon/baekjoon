n = int(input())
result = []
for case in range(n):
    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,input().split())
    dist_1= ((x_1-x_2)**2+(y_1-y_2)**2)**0.5
    dist_2 = abs(r_1+r_2)

    if (dist_1>dist_2):
        result.append(0)
    elif (dist_1==dist_2):
        result.append(1)
    elif (dist_1<dist_2):
        if r_1 < r_2:
            longer = r_2
            shorter = r_1
        elif r_1 >= r_2 :
            longer = r_1
            shorter = r_2

        if dist_1 +  shorter > longer:
            result.append(2)
        elif dist_1 + shorter == longer:
            if r_1==r_2:
                result.append(-1)
            else : result.append(1)
        else :
            result.append(0)

for i in result:
    print(i)