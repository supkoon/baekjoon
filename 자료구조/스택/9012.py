n = int(input())

results = []
for case in range(n):
    stack = []
    ins = str(input())
    result = 'YES'
    for i in ins:
        if i =='(':
            stack.append(i)
        else : # ')'
            if len(stack) ==0 :
                result = 'NO'
                break
            else :
                stack.pop()
    if len(stack) !=0 :
        result = "NO"
    results.append(result)
for i in results:
    print(i)