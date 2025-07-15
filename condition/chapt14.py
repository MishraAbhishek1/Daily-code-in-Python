# Problem 2: Role-Based Dashboard Access

role = input("Enter your role (admin/staff/student): ").lower()

if role == "admin":
    print("Welcome to Admin Dashboard 🛠️")
elif role == "staff":
    print("Welcome to Staff Dashboard 📊")
elif role == "student":
    print("Welcome to Student Panel 📚")
else:
    print("Invalid Role ❌")