n = int(input())

a = list(map(int,input().split()))
max = max(a)
for i in range(n):
    a[i] = a[i]/max*100

print(sum(a)/len(a))