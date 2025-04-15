def comb_sort(array):
    n = gap = len(array)
    check_swap = True

    while gap > 1 or check_swap:
        check_swap = False
        gap = int(gap * 10 / 13)  # shrink = 1.3으로 설정
        if gap < 1:
            gap = 1

        for i in range(n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                check_swap = True
    return array