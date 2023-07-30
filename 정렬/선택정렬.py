# arr = [7,5,9,0,3,1,6,2,4,8]


# def sort():
#     for i in range(len(arr)):
#         min_idx = i 
#         for j in range(i+1,len(arr)):
#             if arr[min_idx] > arr[j]:
#                 arr[min_idx], arr[j] = arr[j], arr[min_idx]
# sort()
# print(arr)





'''
선택정렬 복습

가장 기본적인 O(n^2) 정렬방법

'''


arr = [7,5,9,0,3,1,6,2,4,8]


for i in range(0,len(arr)):
    min_idx = i 
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx = j
    arr[min_idx],arr[i] = arr[i],arr[min_idx]

print(arr)
            

