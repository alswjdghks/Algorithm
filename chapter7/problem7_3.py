n,m = map(int,input().split())
riceCake = list(map(int,input().split()))

riceCake.sort()
max_high = max(riceCake)
riceCake_list = [ (x-max_high) for x in riceCake if x >= max_high]

while sum(riceCake_list) < m:
    max_high -= 1
    riceCake_list = [ (x-max_high) for x in riceCake if x >= max_high]

print(max_high)

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None