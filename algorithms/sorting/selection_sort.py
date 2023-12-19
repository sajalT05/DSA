"""
sort an array of N integers.
"""
from typing import List


input_array = [13,46,24,52,20,9]
ARRAY_LENGTH = len(input_array)

def selection_sort(array: List[int]) -> List[int]:
    '''get lowest number to the pivot index.'''
    for i in range(ARRAY_LENGTH):
        min_idx = i
        for j in range(i+1,ARRAY_LENGTH):
            if array[j]<=array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array

print(selection_sort(array=input_array))
