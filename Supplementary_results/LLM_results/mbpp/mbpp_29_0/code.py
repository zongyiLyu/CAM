## main.py

def comb_sort(arr: list) -> list:
    """
    Sorts a list using the comb sort algorithm.

    Parameters:
    arr (list): A list of elements (integers, floats, strings) to be sorted.

    Returns:
    list: A new list containing the sorted elements.
    """
    # Initialize the gap and the sorted flag
    gap = len(arr)
    shrink = 1.3  # Shrink factor
    sorted_flag = False

    # Create a copy of the original array to avoid modifying it
    sorted_arr = arr.copy()

    while not sorted_flag:
        # Update the gap for the next comb
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        
        sorted_flag = True  # Assume the array is sorted

        # Compare elements with the current gap
        for i in range(len(sorted_arr) - gap):
            if sorted_arr[i] > sorted_arr[i + gap]:
                # Swap the elements if they are in the wrong order
                sorted_arr[i], sorted_arr[i + gap] = sorted_arr[i + gap], sorted_arr[i]
                sorted_flag = False  # We made a swap, so the array is not sorted yet

    return sorted_arr
