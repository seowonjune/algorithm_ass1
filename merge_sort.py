# base merge sort
'''
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    return merge(left_array, right_array)

def merge(left, right):
    i, j = 0,0
    sorted_array = []
    
    while i < len(left) and j < len(right):
    	if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array
'''

# for test code -> stable sort 확인
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left_array = merge_sort(left)
    right_array = merge_sort(right)
    return merge(left_array, right_array)

def merge(left, right):
    i, j = 0, 0
    sorted_array = []

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

