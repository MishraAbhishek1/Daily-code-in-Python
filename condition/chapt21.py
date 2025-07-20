# ✅ Problem 21: Multiple Login Attempts

attempts = 3

for iteration in range(attempts):
    password = str(input("Enter Your Password: "))
    if password == "alpha":
        print("Access Granted")
        break
else:
    print("account Locked")        