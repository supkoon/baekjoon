arr = [7,5,9,0,3,1,6,2,4,8]


def sort():
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                arr[min_idx], arr[j] = arr[j], arr[min_idx]
sort()
print(arr)