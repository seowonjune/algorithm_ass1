'''
Leaf 노드에 배열 값을 배치
부모 노드는 두 자식 중 작은 값을 선택해서 저장
트리의 루트에 있는 값이 현재 최소값
이 값을 정렬 결과에 추가하고, 해당 leaf 값을 무한대로 바꿈
다시 트리를 재정렬 함
전체 배열이 소모될 때까지 반복'''

import math

def tournament_sort(array):
    for i in range(len(array)):
        if not isinstance(array[i], tuple):
            array[i] = (array[i], i)
    n = len(array)
    if n == 0:
        return []

    tree = [0] * (2 * n - 1)

    for i in range(n):
        tree[n - 1 + i] = (array[i][0], i)  # value만 가져와 tree에 저장

    for i in range(n - 2, -1, -1):
        left = tree[2 * i + 1]
        right = tree[2 * i + 2]
        tree[i] = left if left[0] <= right[0] else right

    sorted_array = []
    for _ in range(n):
        value, index = tree[0]
        sorted_array.append((value, index))  # ✅ 튜플 전체를 저장

        pos = n - 1 + index
        tree[pos] = (float('inf'), index)

        while pos > 0:
            parent = (pos - 1) // 2
            left = tree[2 * parent + 1]
            right = tree[2 * parent + 2]
            tree[parent] = left if left[0] <= right[0] else right
            pos = parent

    return sorted_array
