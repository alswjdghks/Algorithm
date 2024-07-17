n = int(input())
market = list(map(int,input().split()))
m = int(input())
costomer = list(map(int,input().split()))

market.sort()

def binarySearch(array,num,start,end):
    if start > end:
        return False 
    mid = (start + end) // 2
    if array[mid] == num:
        return True
    elif array[mid] > num:
        return binarySearch(array,num,start,mid-1)
    else:
        return binarySearch(array,num,mid+1,end)
def binarySearch2(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in costomer:
    result = binarySearch2(market,i,0,len(market)-1)
    if result == None:
        print("no",end=" ")
    else:
        print("yes",end=" ")