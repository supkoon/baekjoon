import sys
results = []
for sentence in sys.stdin:
    if sentence =='.\n':
        break
    stack =[]
    result = 'yes'
    for i in list(sentence):
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack) ==0:
                result = 'no'
                break
            o = stack.pop()
            if o != '(':
                result = 'no'
        elif i==']':
            if len(stack) ==0:
                result = 'no'
                break
            o = stack.pop()
            if o!= '[':
                result = 'no'
    if len(stack)!=0:
        result = 'no'
    results.append(result)

for i in results:
    print(i)




