
routes = []

def shortest_path(mat, route, r, c):
    # Base case
    if not mat or not len(mat):
        return

    num_rows = len(mat)
    num_cols = len(mat[0])

    route.append(mat[r][c])

    if r == num_rows - 1 and c == num_cols - 1:
        routes.append(route.copy())
    else:
        # move down
        if r + 1 < num_rows:
            shortest_path(mat, route, r + 1, c)

        # move right
        if c + 1 < num_cols:
            shortest_path(mat, route, r, c + 1)

        # move diagonally
        if r + 1 < num_rows and c + 1 < num_cols:
            shortest_path(mat, route, r + 1, c + 1)

    route.pop()


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

shortest_path(mat, [], 0, 0)

for r in routes:
    print(r)
