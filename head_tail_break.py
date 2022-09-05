def head_tail_break(data = []):
    output = []

    def recursive_call(data):
        ave = 0

        for d in data:
            ave += d

        ave = ave / len(data)

        head = []
        output.append(ave)

        for d in data:
            if d > ave:
                head.append(d)

        condition = len(head) > 1 and len(head) / len(data) < 0.4

        while condition:
            recursive_call(head)

    recursive_call(data)

    return output

data = [5, 10, 12, 13, 15, 11, 10, 8, 6, 3, 2, 2, 2, 2, 1, 1, 1, 1]
print("Distribution:")
print(data)

breakpoints = head_tail_break(data)
print("Breakpoints:")
print(breakpoints)
