def check_han(a):
    a = str(a)
    result = []
    for i in range(len(a)-1):
        result.append(int(a[i+1])-int(a[i]))
    if (len(set(result)) == 1) | (len(a)==1):
        return 1
    else : return 0

result = 0
for i in range(1,int(input())+1):
    result+=check_han(i)

print(result)





