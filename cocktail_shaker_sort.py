def cocktail_shaker_sort(array):
    n = len(array)
    start, end = 0, n-1

    while start < end:
        chek_swap = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                chek_swap = True
        end -= 1

        for j in range(end, start, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                chek_swap = True
        start += 1
        if not chek_swap:
            break
    return array
