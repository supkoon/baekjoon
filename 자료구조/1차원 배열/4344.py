
a = int(input())
result = []
for i in range(a):

    b = list(map(int,input().split()))
    total = b.pop(0)
    avg_score = sum(b)/total
    c = [i for i in b if i > avg_score]
    result.append(len(c)/total*100)

for i in result:
    print("%0.3f%%"%(i))

# for i in result:
#     print(f"{i:0.3f}%")