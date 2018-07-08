"""
Problem 11 - Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been marked in
red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?

Note: The grid is in the file 11.txt4
"""


def parse_grid(lines):
    grid = []
    for line in lines:
        row = []
        for i in line.rstrip('\n').split():
            row.append(int(i))
        grid.append(row)
    return grid


if __name__ == '__main__':
    grid = parse_grid(open('11.txt').readlines())
    greatest = 0

    # HORIZONTAL
    for i in range(len(grid)):
        for j in range(len(grid) - 3):
            n = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if n > greatest:
                greatest = n

    # VERTICAL
    for i in range(len(grid) - 3):
        for j in range(len(grid)):
            n = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if n > greatest:
                greatest = n

    # DIAGONAL from T-L to B-R
    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            n = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if n > greatest:
                greatest = n

    # DIAGONAL from T-R to B-L
    for i in range(len(grid) - 3):
        for j in range(3, len(grid)):
            n = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            if n > greatest:
                greatest = n

    print(greatest)
