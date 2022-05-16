from collections import Counter
import sys
n =  int(sys.stdin.readline())
result = []
for _ in range(n):
    result.append(int(sys.stdin.readline()))
result= sorted(result)
sys.stdout.write(str(round(sum(result)/n))+"\n")
sys.stdout.write(str(result[len(result)//2])+"\n")
counter = Counter(result).most_common()
if (len(counter)>1) and (counter[0][1] == counter[1][1]):
    sys.stdout.write(str(counter[1][0])+"\n")
else : sys.stdout.write(str(counter[0][0])+"\n")
sys.stdout.write(str(max(result)-min(result))+"\n")

