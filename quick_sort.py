def quick_sort(array):
    if len(array) < 2:
        return

    count = [(0, len(array) - 1)]

    while count:
        start, end = count.pop()
        if start >= end:
            continue

        pivot = start
        low = start + 1
        high = end

        while low <= high:
            while low <= end and array[low][0] <= array[pivot][0]:
                low += 1
            while high > start and array[high][0] >= array[pivot][0]:
                high -= 1

            if low > high:
                array[high], array[pivot] = array[pivot], array[high]
            else:
                array[low], array[high] = array[high], array[low]

        count.append((start, high - 1))
        count.append((high + 1, end))


def get_sort_function():
    def sorting(array):
        quick_sort(array)
    return sorting
