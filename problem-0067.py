"""
Problem 67 - Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in '67.txt' a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2**99 altogether! If you
could check one trillion (10**12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
"""


def parse_triangle(lines):
    triangle = []
    for line in lines:
        row = []
        for i in line.rstrip('\n').split():
            row.append(int(i))
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    triangle = parse_triangle(open('67.txt').readlines())
    rows = len(triangle)
    while rows > 1:
        i = rows - 2
        for j in range(i+1):
            triangle[i][j] += max((triangle[i+1][j], triangle[i+1][j+1]))
        triangle.pop()
        rows -= 1

    print(triangle[0])
