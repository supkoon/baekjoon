class Stack:
    def __init__(self):
        self.attributes = []
    def push(self,n):
        self.attributes.append(n)
    def pop(self):
        if len(self.attributes)!=0:
             return(self.attributes.pop())
        else : return -1
    def size(self):
        return len(self.attributes)
    def empty(self):
        if len(self.attributes)==0:
            return 1
        else : return 0
    def top(self):
        if self.empty():
            return -1
        else: return self.attributes[self.size()-1]

import sys
n = int(sys.stdin.readline())
stack = Stack()
results=[]
for case in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(command[1])
    else :
        result = getattr(stack,command[0])
        result = result()
        results.append(result)

for i in results:
    sys.stdout.write(str(i) + '\n')







