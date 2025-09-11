from datetime import datetime

date_str = "2025-09-10 14:30:00"   # yeh ek string hai
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print(parsed)
print(type(parsed))
