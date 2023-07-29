arr = [7,5,9,0,3,1,6,2,4,8]


for i in range(len(arr)):
    for j in range(i,0,-1): #1까지만 돌려야 j-1과 비교가능 
        if arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j],arr[j-1]
        else:
            break #앞에는 이미 정렬되어있어서 안되는순간 다음인덱스

print(arr)