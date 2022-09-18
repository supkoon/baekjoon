import sys
class Queue():
    def __init__(self):
        self.a = []
        self.cnt =0
    def push(self,n):
        self.a.append(n)
    def pop(self):
        if len(self.a) > self.cnt:
            out = self.a[self.cnt]
            self.cnt += 1
            return out
        else : return -1
    def size(self):
        return len(self.a)-self.cnt
    def empty(self):
        return 1 if len(self.a)==self.cnt else 0
    def front(self):
        return self.a[self.cnt] if len(self.a)>self.cnt else -1
    def back(self):
        return self.a[-1] if len(self.a)>self.cnt else -1

q = Queue()
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0]=='push':
        q.push(order[1])
    elif order[0]=='pop':
        sys.stdout.write(str(q.pop())+'\n')
    elif order[0]=='size':
        sys.stdout.write(str(q.size())+'\n')
    elif order[0]=='empty':
        sys.stdout.write(str(q.empty())+'\n')
    elif order[0]=='front':
        sys.stdout.write(str(q.front())+'\n')
    elif order[0]=='back':
        sys.stdout.write(str(q.back())+'\n')
