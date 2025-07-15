# ✅ Problem 1: Email Already Exists Check (Signup system)

emails = input("Enter your email address: ")
existing_emails = ["test@gmail.com", "admin@site.com", "user1@mail.com"]

if emails in existing_emails:
    print("Email already exists. Please use a different email.")
else:
    print("Email is avaialble for registration.")   