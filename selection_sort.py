
def fn_swap(some_array, index_a, index_b):
    temp_char = some_array[index_a]
    some_array[index_a] = some_array[index_b]
    some_array[index_b] = temp_char

def selection_sort_recursive(some_array, index, length):
    # Find the minimum element in the subarray [index...length - 1]
    minimum_index = index

    for i in range(minimum_index + 1, length):
        if some_array[i] < some_array[minimum_index]:
            minimum_index = i

    fn_swap(some_array, minimum_index, index)

    if index + 1 < length:
        selection_sort(some_array, index + 1, length)

def selection_sort(some_array):
    for i in range(len(some_array) - 1):
        minimum_index = i

        for j in range(i + 1, len(some_array)):
            if some_array[j] < some_array[minimum_index]:
                minimum_index = j

        fn_swap(some_array, minimum_index, i)

the_array = [5, 1, 3, 5, 6, 2, 9]
print(the_array)
#selection_sort_recursive(the_array, 0, len(the_array))
selection_sort(the_array)

print(the_array)
