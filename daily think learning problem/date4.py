# 5. Real-World Example (Subscription Expiry)

"""from datetime import datetime
from dateutil.relativedelta import relativedelta

signup_date = datetime(2025, 9, 12)
plan_duration = relativedelta(months=6)  # 6 month plan

expiry_date = signup_date + plan_duration
print("Expiry Date:", expiry_date)

# Check if expired
today = datetime.now()
if today > expiry_date:
    print("Plan expired")
else:
    print("Plan active")
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

signup_date = datetime(2026, 1, 1)
plan_duration = relativedelta(month=6) # 6 month plan

expiry_date = signup_date + plan_duration
print("Expiry Date:", expiry_date)

# now we check Expired or not Expired in Conditions
today = datetime.now()
if today > expiry_date:
    print("Your Plan is Expired Please Renew")
else:
    print("Your Plan is Active Ednjoy Your Service")    