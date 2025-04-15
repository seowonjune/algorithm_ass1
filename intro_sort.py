'''
Quick Sort로 시작
재귀 깊이를 추적 (2 * log₂(n)을 한계로 설정)
그걸 넘으면 → Heap Sort로 전환
작은 배열은 → Insertion Sort로 정리'''

import math

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        target_array = array[i]
        j = i - 1
        while j >= left and array[j] > target_array:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = target_array

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array, start, end):
    target_array = array[start:end+1]
    n = len(target_array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(target_array, n, i)
    for j in range(n - 1, 0, -1):
        target_array[j], target_array[0] = target_array[0], target_array[j]
        heapify(target_array, j, 0)

    array[start:end+1] = target_array


def quick_sort_intro(array, left, right, depth_limit):
    if right - left <= 16:
        insertion_sort(array, left, right)
        return
    if depth_limit == 0:
        heap_sort(array, left, right)
        return

    pivot = array[left]
    low = []
    high = []

    for i in range(left + 1, right + 1):
        if array[i] < pivot:
            low.append(array[i])
        else:
            high.append(array[i])

    mid = left + len(low)
    array[left:right + 1] = low + [pivot] + high

    quick_sort_intro(array, left, mid - 1, depth_limit - 1)
    quick_sort_intro(array, mid + 1, right, depth_limit - 1)

def intro_sort(array):
    n = len(array)
    depth_limit = int(2 * math.log2(n)) if n > 0 else 0
    quick_sort_intro(array, 0, n - 1, depth_limit)
    return array
