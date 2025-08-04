# Part 2: Intermediate Loop Concepts
# Now let’s level up with more practical examples.
# 4. Nested Loops
# A loop inside another loop, used for multidimensional data.


# Example 6: Printing a 2D Matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()    