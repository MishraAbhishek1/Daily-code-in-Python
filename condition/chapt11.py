#User Role Based Page Access
role = str(input("Enter yours role (admin/user/guest): "))

# making a decission box where we select the page based on the role
if role == "admin":
    print("You can access all pages")
elif role == "user":
    print("You can access user page")
elif role == "guest":
    print("You can access guest apge")    
else:
    print("You have no permission because no role matched")        