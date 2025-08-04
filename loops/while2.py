# Real-World Use: In a SaaS app, you might use a while loop to poll an API until it returns a response.
# Example 4: Polling API

attempts = 0
max_attempts = 3

while attempts <= max_attempts:
    print(f"Attempt {attempts+1}: Checking API....")
    attempts += 1
