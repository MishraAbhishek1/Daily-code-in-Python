import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your@email.com", "wrongpassword")
except smtplib.SMTPAuthenticationError:
    print("❌ Authentication failed. Check username or password.")
