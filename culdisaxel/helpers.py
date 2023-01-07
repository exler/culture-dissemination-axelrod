def get_grid_neighbors(n: int, index: tuple[int, int]) -> tuple[tuple[int, int]]:
    """
    Gets the top, right, bottom and left neighbors of the cell at the given index.

    If the cell is on the edge of the grid, only the neighbors that are on the grid are returned.
    """
    x, y = index
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))

    if x < n - 1:
        neighbors.append((x + 1, y))

    if y > 0:
        neighbors.append((x, y - 1))

    if y < n - 1:
        neighbors.append((x, y + 1))

    return tuple(neighbors)
