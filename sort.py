#!/usr/bin/env python3
# -*-coding:UTF-8 -*

from utils import real

def partition_list(array: list[real], start_index: int = 0, end_index: int = None, order: int = 0, pivot_index: int = None) -> int:
    """
    Rearranges elements in a sublist of 'array' such that all elements less than the pivot are before it,
    and all elements greater than or equal to the pivot are after it if 'order' is 0. If 'order' is 1, the
    opposite arrangement is applied. The function operates in-place and returns the final index of the pivot element.
    
    Parameters:
    array (list[real]): The list of elements to be partitioned.
    start_index (int): The starting index of the sublist to partition.
    end_index (int): The ending index of the sublist to partition.
    order (int): Determines the order of arrangement; 0 for less than pivot first, 1 for greater first.
    pivot_index (int): The index of the pivot element.
    
    Returns:
    int: The final index position of the pivot element after partitioning.
    
    Time Complexity: O(n), where n is the number of elements in the sublist.
    Space Complexity: O(1), as the rearrangement is done in-place without using extra space.
    
    Note:
    The function optimizes space complexity by modifying the list in-place. However, time complexity may
    worsen due to swaps.
    """
    assert start_index >= 0
    len_array = len(array)
    if end_index == -1:
        end_index = len_array
    assert end_index > start_index
    if pivot_index != -1:
        assert start_index <= pivot_index < end_index
        array[pivot_index], array[end_index - 1] = array[end_index - 1], array[pivot_index]
    
    pivot_value = array[end_index - 1]
    new_pivot_index = start_index  # Initialize the position of the pivot
    
    for current_index in range(start_index, end_index - 1):
        if (array[current_index] < pivot_value) + order == 1:
            # In the case order = 0, the process is done in the increasing order, while it's done in the decreasing one int the case order = 1
            array[new_pivot_index], array[current_index] = array[current_index], array[new_pivot_index]
            new_pivot_index += 1
    
    array[new_pivot_index], array[end_index - 1] = array[end_index - 1], array[new_pivot_index]
    return new_pivot_index

def quick_sort(datas: list[real], start_index: int = 0, end_index: int = None, order: int = 0, pivot_index: int = None) -> None:
    """
    Sorts a sublist of 'datas' from 'start_index' to 'end_index' using the Quick Sort algorithm.
    The sorting order is ascending if 'order' is 0 and descending if 'order' is 1.

    Parameters:
    datas (list[real]): The list of elements to be sorted, which can contain real numbers or strings.
    start_index (int): The starting index of the sublist to sort.
    end_index (int): The ending index of the sublist to sort; defaults to the length of the list.
    order (int): Sorting order flag; 0 for ascending, 1 for descending.
    pivot_index (int): The index of the pivot element; defaults to the last element of the sublist.

    Returns:
    None: The function sorts the list in place and does not return anything.

    Time Complexity: O(n log n) on average, where n is the number of elements in the sublist.
    Space Complexity: O(log n), which is the stack space used by recursive calls.

    Note:
    This implementation uses the 'partition_list' function to optimize space complexity.
    """
    assert start_index >= 0  # Ensure the start index is non-negative

    if end_index is None:
        end_index = len(datas)

    # Base case: if the sublist is empty or has one element, it's already sorted
    if end_index <= start_index + 1:
        return

    # If 'pivot_index' is not provided, use the last element as the pivot
    if pivot_index is None:
        pivot_index = end_index - 1
    else:
        # Ensure the pivot index is within the bounds of the sublist
        assert start_index <= pivot_index < end_index

    # Partition the list and get the position of the pivot after partitioning
    pivot_final_index = partition_list(datas, start_index, end_index, order, pivot_index)

    # Recursively apply quick sort to the sublists before and after the pivot
    quick_sort(datas, start_index, pivot_final_index, order)
    quick_sort(datas, pivot_final_index + 1, end_index, order)


if __name__ == "__main__":
    import sort
    print(help(sort))