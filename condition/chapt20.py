# ✅ Problem 19: License Eligibility
age = int(input("Enter your Age: "))
vision = input("Do you have a Clear Vision? (yes/no): ")

if age >= 18:
    if vision == "yes":
        print("You are Eligible for License")
    else:
        print("Eye Test are needed for License Eligibility")
else:
    print("Underage")            