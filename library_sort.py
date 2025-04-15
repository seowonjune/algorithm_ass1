# insertion sort에 gap을 넣은거

def insertion_sort_lib(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i - 1

        while j>=0 and array[j] > temp:
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp
    return array


def library_sort(array):
    n = len(array)
    if n < 2:
        return array
    
    gap_array = [0] * 2 * n

    gap_array[0] = array[0]
    cnt = 1

    for i in range(1, n):
        if cnt >= len(gap_array) // 2:
            gap_array = rebalancing(gap_array, cnt)

        new_position = binary_search(gap_array, array[i], cnt)

        shift(gap_array, new_position, cnt)

        gap_array[new_position] = array[i]
        cnt += 1

        sorted_array = []
        for x in gap_array:
            if x != 0:
                sorted_array.append(x)
    return sorted_array

def binary_search(array, target, cnt): 
    left=0
    right = cnt - 1

    while left <= right:
        mid = (left + right) // 2
       
        if array[mid] == 0:
            for i in range(mid, -1, -1):
                if array[i] != 0:
                    mid = i
                    break
            else:
                for i in range(mid + 1, cnt):
                    if array[i] != 0:
                        mid = i
                        break
                else:
                    return 0
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def shift(array, index, cnt):
    gap_index = cnt
    while gap_index < len(array) and array[gap_index] != 0:
        gap_index += 1

    if gap_index >= len(array):
        gap_index = len(array) - 1

    while gap_index > index:
        if gap_index -1 >= 0 and array[gap_index-1] != 0:
            array[gap_index] = array[gap_index-1]
        gap_index -= 1

def rebalancing(array, cnt):
    elements = [x for x in array if x != 0]
    insertion_sort_lib(elements)

    new_size = 2 * len(elements)
    new_array = [0] * new_size

    gapping = new_size / len(elements)

    for i in range(len(elements)):
        pos = int(i * gapping)
        new_array[pos] = elements[i]
    return new_array
