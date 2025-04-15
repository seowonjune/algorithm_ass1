run_step = 16

def insertion_sort_tim(array, left, right):
    for i in range(left + 1, right):
        while i > left and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1

def merge_sort_tim(array, left, mid, right):
    array1 = array[left:mid]
    array2 = array[mid:right]
    index1 = index2 = 0
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            array[left] = array1[index1]
            index1 += 1
        else:
            array[left] = array2[index2]
            index2 += 1
        left += 1
    for i in range(index1, len(array1)):
        array[left] = array1[i]
        left += 1
    for i in range(index2, len(array2)):
        array[left] = array2[i]
        left += 1

def run_size(n):
    alpha = 0
    while n > run_step:
        if alpha == 0 and n % 2:
            alpha = 1
        n //= 2
    return n + alpha


def tim_sort(array):
    n = len(array)
    run = run_size(n)

    for low in range(0, n, run):
        high = min(low + run, n)
        insertion_sort_tim(array, low, high)

    while run < n:
        for low in range(0, n, run * 2):
            mid = low + run
            high = min(mid + run, n)
            merge_sort_tim(array, low, mid, high)
        run *= 2
    
    return array