# Validate User Input (SaaS)

attempts = 3
while attempts >= 0:
    password = input("Enter your password: ")
    if password == "1234":
        print("Access Granted")
        continue
    attempts -= 1
    if attempts != -1:
       print(f"{attempts} left attempts: ")
else:
  print("Access Denied")
