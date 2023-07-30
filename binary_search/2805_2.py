'''
문제
나무자르기
나무 M미터가 필요함. 

절단기 높이 h 설정. --> 한 줄을 해당 높이로 자름 --> 적어도 m미터를 가져가기 위한 최대높이 h는 무엇인가?


아이디어
m의 범위가 매우 크기 때문에, 이분탐색을 고려해야함. 
높이 개념은 정렬되어 있기 때문에, 이분탐색을 사요할 수 있어보인다.  


복잡도 
O(lon2n)


'''

n, m =map(int,input().split())
trees = list(map(int,input().split()))

max_h = 0
def bisec(arr,target,start,end):
    global max_h 


    if start>end:
        #이전(start==end)에도 result가 더 컸는데, 다음 범위에서는 start+1,end가 되어 넘어버림. 이전 것 리턴. 
        # max_h = end
        return end
    
    mid = (start+end)//2
    
    result = 0
    for tree in trees:
        result += max(0,tree-mid)

    if result == target:
        max_h= mid
        return mid 

    elif result > target:
        max_h = mid
        #최대한 덜 잘랐을때가 정답이니깐. 
        return bisec(arr,target,mid+1,end)
    else:
        return bisec(arr,target,start,mid-1)
    
print(bisec(trees, m, 0, max(trees)+1))
