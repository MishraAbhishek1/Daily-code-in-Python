# 10. Infinite Loops with while
# Used for continuous processes (e.g., AI agents or servers).

# Example 12: Simple Server Loop
while True:
    user_input = input("Enter a Command (or 'exit' to quit): ")
    if user_input == 'exit':
        break
    print(f"Recieved; {user_input}")