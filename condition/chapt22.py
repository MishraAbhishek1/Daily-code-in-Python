# 🔐 ✅ Real-World Project: ATM Login System
print("Welcome to Alpha Bank ATM")
correct_pin = 123456
max_attempts = 3

for attempt in range(max_attempts):
    entered_pin = int(input("Enter your 4-digit PIN: "))

    if entered_pin == correct_pin:
        print("Access granted ")
        break
    else:
        print("Incorect PIN")
else:
    print("ATM card Blocked due to 3 wrong Attempts. Contact Your Bank")        