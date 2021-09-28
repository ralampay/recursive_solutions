
def is_palindrome_exhaustive(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False

        i = i + 1
        j = j - 1

    return True

def is_palindrome_recursive(s, l, h):
    # Base case
    if l >= h:
        return True

    # No match will return false
    if s[l] != s[h]:
        return False

    # Recursive case by closing in the middle
    return is_palindrome_recursive(s, l + 1, h - 1)

s = 'XYBYX'
print(is_palindrome_recursive(s, 0, len(s) - 1))
