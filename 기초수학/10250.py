n = int(input())
# 입력 H W N
# 출력 N번째 손님에 배정되어야 하는 방 번호
result = []
for i in range(n):
    H,W,N = list(map(int,input().split()))

    if N%H == 0:
        last = N//H
    else :
        last = N//H +1

    if last <10:
        last = str(0)+str(last)

    if N%H ==0 :
        first = H
    else :
        first = N%H

    room = f"{first}{last}"
    result.append(room)

for i in result:
    print(i)