# 6. Authentication System (Wrong Password Handling)
try:
    password = input("Enter your password: ")
    if password != "admin123":
        raise ValueError("Incorrect password! this is a custom error message")
    print("Access granted. ")
except ValueError as e:
    print("Error: ", e)    