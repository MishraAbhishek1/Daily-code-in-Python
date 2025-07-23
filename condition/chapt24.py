# ✅ Problem 25: Gender-Based Form Input

gender = str(input("Enter The Gender (M/F/O): ")).upper()

if gender == 'M':
    print("Hello Sir How Can I help you")
elif gender == 'F':
    print("Hello Mam How can I Help You")
elif gender == 'O':
    print("Hello Friend")
else:
    print("Invalid Gender")            