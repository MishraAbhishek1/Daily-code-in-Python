def print_stars(n):
    # Time Complexity: O(n) -> loop runs n times
    # Space Complexity: O(1) -> no extra memory used

    for i in range(n):   # loop runs n times
        print("*", end=" ")
    print()

print_stars(5)
