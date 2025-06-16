# Python Programming Using Strip ()

role = input("Enter your Role->(HR or Interviewer): ")

cleaned_role = role.strip()

if cleaned_role == "HR":
    print("HR Registered Succesfully")
elif cleaned_role == "Interviewer":
    print("Interviewer Registerd Succesfully")
else:
    print("Invalid Role (Please Enter a Valid Role -> HR Or Interviewer)")        