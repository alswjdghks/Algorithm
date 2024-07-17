array = [7,5,9,0,3,1,6,2,4,8]
array2 = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
                array[i],array[j] = array[j],array[i]  #swap
    return array

def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break
    return array

def quick_sort(array,start,end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right],array[pivot] = array[pivot],array[right]
        else:
            array[left],array[right] = array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    return array

def quickSort(array):
    if len(array) == 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x> pivot]
    return quickSort(left_side) + [pivot] + quickSort(right_side)

def counting_sort(array):
    count = [0] * 10
    index = 0
    for x in array:
        count[x] += 1
    for i in range(10):
        for j in range(count[i]):
            array[index] = i
            index += 1
    return array

#print(quick_sort(array,0,len(array)-1))
print(counting_sort(array2))