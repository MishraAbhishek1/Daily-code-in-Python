✅ Day 1: strip()
Q: User se naam lo jo galti se spaces ke sath diya ho, usse clean karke "Welcome, <name>" print karo.

python
Copy
Edit
name = input("Enter your name: ")  # e.g. "   Rahul  "
clean_name = name.strip()
print(f"Welcome, {clean_name}")
✅ Day 2: lower()
Q: Email ID check karo agar woh lowercase mein nahi hai, toh usse lowercase bana do.

python
Copy
Edit
email = input("Enter your email: ")  # e.g. "Rahul@Gmail.com"
print("Processed Email:", email.lower())  # Output: rahul@gmail.com
✅ Day 3: upper()
Q: Kisi user ka username uppercase mein convert karke save karo.

python
Copy
Edit
username = input("Enter username: ")  # e.g. "alpha"
print("Username saved as:", username.upper())  # Output: ALPHA
✅ Day 4: capitalize()
Q: User ka naam leke uska sirf pehla letter capital karo.

python
Copy
Edit
name = input("Enter your name: ")  # e.g. "ravi"
print("Formatted Name:", name.capitalize())  # Output: Ravi
✅ Day 5: title()
Q: Sentence lo jisme har word small ho aur use title case mein convert karo.

python
Copy
Edit
line = input("Enter a sentence: ")  # e.g. "python is powerful"
print(line.title())  # Output: Python Is Powerful
✅ Day 6: replace()
Q: "Hello Bro" ko "Hello Bhai" mein convert karo.

python
Copy
Edit
text = "Hello Bro"
print(text.replace("Bro", "Bhai"))  # Output: Hello Bhai
✅ Day 7: split()
Q: Comma-separated string of fruits lo aur list mein tod do.

python
Copy
Edit
fruits = "apple,banana,mango"
fruit_list = fruits.split(",")
print(fruit_list)  # ['apple', 'banana', 'mango']
✅ Day 8: join()
Q: List of names ko ek hi string bana do with | separator.

python
Copy
Edit
names = ['Ravi', 'Amit', 'Neha']
print(" | ".join(names))  # Output: Ravi | Amit | Neha
✅ Day 9: startswith()
Q: Check karo agar string "Hello World" se start ho rahi hai.

python
Copy
Edit
text = "Hello World"
print(text.startswith("Hello"))  # True
✅ Day 10: endswith()
Q: Email ID check karo agar woh '@gmail.com' pe end ho rahi hai.

python
Copy
Edit
email = "rahul@gmail.com"
print(email.endswith("@gmail.com"))  # True
✅ Day 11: isdigit()
Q: User se input lo aur check karo wo number hai ya nahi.

python
Copy
Edit
age = input("Enter your age: ")
print("Valid age:", age.isdigit())  # True if input is all digits
✅ Day 12: isalpha()
Q: Input string mein sirf alphabets hain ya nahi?

python
Copy
Edit
name = input("Enter name: ")  # e.g. "Ravi"
print("Only alphabets:", name.isalpha())  # True
✅ Day 13: isalnum()
Q: Password mein only alphanumeric allowed hai — check karo.

python
Copy
Edit
password = input("Enter password: ")  # e.g. "pass123"
print("Valid password:", password.isalnum())  # True
✅ Day 14: count()
Q: "banana" word mein "a" kitni baar aaya hai?

python
Copy
Edit
word = "banana"
print("Count of 'a':", word.count("a"))  # 3
✅ Day 15: find()
Q: "hello world" mein 'o' pehli baar kis index pe hai?

python
Copy
Edit
text = "hello world"
print("Index of 'o':", text.find("o"))  # 4