n = int(input())
answer = []
stack = []
process =''
success = True
for i in range(n):
    answer.append(int(input()))
sorted_nums = sorted(answer)
stack_pointer = 0
for i in range(n):
    if stack_pointer < n:
        while(True):
            if answer[i] < sorted_nums[stack_pointer]:
                poped = stack.pop()
                process += '-'
                if poped != answer[i]:
                    success = False
                break

            elif answer[i] > sorted_nums[stack_pointer]:
                stack.append(sorted_nums[stack_pointer])
                process+='+'
                stack_pointer+=1
                if stack_pointer==n:
                    success=False
                    break
            else:
                stack.append(sorted_nums[stack_pointer])
                process+='+'
                poped = stack.pop()
                process+='-'
                stack_pointer += 1
                break
    else:
        poped = stack.pop()
        process+='-'
        if poped != answer[i]:
            success=False

if not success:
    print("NO")
else :
    for i in process:
        print(i)
