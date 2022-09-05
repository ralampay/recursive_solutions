# Write a recursive program to reverse a string

# Input: Word of the day

input_str = "Word of the day"

def fn_swap(char_array, index_a, index_b):
    temp_char = char_array[index_a]
    char_array[index_a] = char_array[index_b]
    char_array[index_b] = temp_char

def fn_reverse(char_array, index_a, index_b):
    if(index_a < index_b):
        fn_swap(char_array, index_a, index_b)
        fn_reverse(char_array, index_a + 1, index_b - 1)

char_array = list(input_str)
fn_reverse(char_array, 0, len(char_array) - 1)

print(char_array)
