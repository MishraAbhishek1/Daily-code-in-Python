# 1. Current Date & Time (logging / timestamps me use hota hai)
from datetime import datetime

now = datetime.now()

print("Current Date & Time:", now)

# now we find tommarrow' date

from datetime import timedelta, datetime

today = datetime.now()

tommarrow = today + timedelta(days=1)

print("Tommarrow's Date:", tommarrow.date())
print("Tommarrow's Date & Time:", tommarrow)

# 2. Date formatting
from datetime import datetime
now = datetime.now()
formmated_date  = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formmatted Date & Time:", formmated_date)