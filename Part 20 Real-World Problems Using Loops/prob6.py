# Retry API Call (SaaS)

attempts = 0

while attempts < 3:
    print("Trying to Connect")
    attempts += 1
    if attempts == 2:
        print("conected!")
        break
else:
    print("Failed To connect")    