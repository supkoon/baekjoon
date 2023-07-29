'''
정렬되어 있는 경우에만 가능.

탐색범위를 절반씩 좁히면서 탐색하는 방법.
현재 target보다 mid가 더 작으면 start를 +1
현재 target보다 mid가 더 크면 end를 -1


범위를 반씩 줄이기 때문에 연산 횟수가 log2n에 비례함 --> 복잡도 O(log(n))

''' 

def binary_search(arr,target,start,end):
    print(start,end)
    if start > end:
        return None

    mid = (start + end)//2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,end)
    
    else:
        return binary_search(arr,target,start,mid-1)

arr = [7,5,9,0,3,1,6,2,4,8]
arr = sorted(arr)

result_idx = binary_search(arr,1,0,len(arr)-1)

if result_idx==None:
    print('없음')
else:
    print(result_idx)