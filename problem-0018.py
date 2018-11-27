"""
Problem 18 - Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

See '18.txt'.

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""


def parse_triangle(lines):
    triangle = []
    for line in lines:
        row = []
        for i in line.rstrip('\n').split():
            row.append(int(i))
        triangle.append(row)
    return triangle


triangle = parse_triangle(open('18.txt').readlines())
rows = len(triangle)
while rows > 1:
    i = rows - 2
    for j in range(i+1):
        triangle[i][j] += max((triangle[i+1][j], triangle[i+1][j+1]))
    triangle.pop()
    rows -= 1

print(triangle[0][0])
