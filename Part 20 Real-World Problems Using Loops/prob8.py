# Filter Active Users (SaaS)

users = [{"name": "Alice", "active":False},{"name": "Bob", "active": False}]
for user in users:
    if user["active"]:
        print(user)
        print(f"Acttive User: {user['name']}")
        break
else:
    print("no user Active")    
