# 3. Loop Control Statements

# break: Exits the loop immediately.
# continue: Skips the current iteration and moves to the next.
# pass: Does nothing, used as a placeholder.

# Example 5: Using break and continue

for i in range(10):
    if i == 6:
        continue
    if i == 8:
        break
    print(i)