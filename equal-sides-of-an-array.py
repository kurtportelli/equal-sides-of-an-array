def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1
