import sys
n = int(sys.stdin.readline())
#카운팅 정렬.
#각 인덱스에 해당하는 수의 개수를 센다.
#앞에서부터 저장된 개수만큼 인덱스를 출력해준다.
count = [0 for i in range(10001)]
for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    for j in range(count[i]):
        sys.stdout.write(str(i)+'\n')






