cache = {}
def unique_path(grid, first=0, second=0):
    if grid[first][second] == 1:
        return 0
    if [first, second] == [len(grid) - 1, len(grid[0]) - 1] and grid[first][second] == 0:
        return 1
    paths1 = paths2 = 0
    def calc_paths(index1, index2):
        if (index1, index2) not in cache:
            cache[(index1, index2)] = unique_path(grid, index1, index2)

        return cache[(index1, index2)]
    if first < len(grid) - 1 and grid[first+1][second] == 0:
        paths1 = calc_paths(first+1, second)

    if second < len(grid[0]) - 1 and grid[first][second+1] == 0:
        paths2 = calc_paths(first, second+1)


    return paths1 + paths2

print(unique_path([[1, 0]]))