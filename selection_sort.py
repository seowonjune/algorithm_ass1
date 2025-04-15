def selection_sort(array):
    n = len(array)

    for i in range(0, n-1):
        min_index = i 
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        array[min_index], array[i] = array[i], array[min_index]
    return array
