@staticmethod
def merge(array1: "Array", array2: "Array")-> "Array":
    """
    Merges two Array objects in a single order fashion. 
    If either array is longer, 
    merge the items in the back of the resulting array.
    Example:
    >>> print(array1)
    [5, 7, 17, 13, 11]
    >>> print(array2)
    [12, 10, 2, 4, 6]
    >>> new_array = Array.merge(array1, array2)
    >>> print(new_array)
    [5, 12, 7, 10, 17, 2, 13, 4, 11, 6]
    Args:
    array1 (Array): The first array to merge.
    array2 (Array): The second array to merge.
    Returns:
    Array: A new array containing the merged elements from
    array1 and array2.
    Raises:
    
    TypeError: If either array1 or array2 are not Array objects """
    pass 