def reverse_array(array: list) -> list:
    """
    Reverse the order of the elements in an array with O(N) linear time complexity and
    Constant space complexity.
    """
    
    start_index = 0
    end_index = len(array) - 1

    while start_index < end_index:
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1

    return array


if __name__ == "__main__":
    print(reverse_array([1, 2, 3, 4, 5]))
    print(reverse_array(['a', 'b', 'c', 'd']))
