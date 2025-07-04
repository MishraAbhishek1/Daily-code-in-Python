# prob21.py - Password validation rules
password = "Alpha123"
print(password.isalnum() and any(c.isdigit() for c in password)and any(c.isalpha() for c in password))