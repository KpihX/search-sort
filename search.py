#!/usr/bin/env python3
# -*-coding:UTF-8 -*

from utils import real

def dich_search(target: real, sequence: list[real], start_index: int = 0, end_index: int = None) -> int:
    """
	Perform a binary search to find the index of 'target' in 'sequence'[start_index: end_index-1].

    Parameters:
    target (real): The value to search for within the sequence.
    sequence (list[real]): An indexable, ordered iterable to search within.
    start_index (int): The starting index of the search range.
    end_index (int): The ending index of the search range (exclusive).

    Returns:
    int: The index of 'target' in 'sequence' if found, otherwise -1.

    Time Complexity: O(log n), where n is the number of elements in the search range.
    Space Complexity: O(1), as the space used does not depend on the size of the input sequence.
    """

    # Ensure the start index is non-negative
    assert start_index >= 0

    # If end_index is not provided, set it to the length of the sequence
    if end_index is None:
        end_index = len(sequence)

    # If the range is invalid, return -1 indicating 'target' is not found
    if start_index >= end_index:
        return -1

    # Calculate the middle index of the current search range
    middle_index = (start_index + end_index) // 2
    middle_value = sequence[middle_index]

    # Check if the middle value is the target
    if middle_value == target:
        return middle_index

    # Determine the direction of the search based on the ordering of the sequence
    if (target - middle_value) * (middle_value - sequence[start_index]) >= 0:
        # Target must be in the second half of the sequence
        return dich_search(target, sequence, middle_index + 1, end_index)
    
    # Target must be in the first half of the sequence
    return dich_search(target, sequence, start_index, middle_index)


if __name__ == "__main__":
	import search
	print(help(search))