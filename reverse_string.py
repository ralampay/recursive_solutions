
def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

    return s

def reverse_string(s, l, h):
    if l < h:
        s = swap(s, l, h)
        return reverse_string(s, l + 1, h - 1)
    return s

data_input = "Hello World"
the_string = []

for o in data_input:
    the_string.append(o)

data_output = reverse_string(the_string, 0, len(the_string) - 1)
print(data_output)
