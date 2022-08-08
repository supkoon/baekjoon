result = [0,1]

for i in range(2,int(input())+1):
    result.append(result[i-1]+result[i-2])
print(result[-1])
