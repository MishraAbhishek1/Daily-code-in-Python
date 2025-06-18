import re

#sample text for atesting purpose
text = """
Contact: john.doe@example.com, phone: 123-456-7890
Website: https://www.example.com"
"""

def chapter1_basic():
    print("=== Chapter 1: Basic Regex Operations")

    #1. find the First occurance ofa pattern using re.search()>>
    print("\n1. Using re.search() to find the first email: ")
    email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"Found email: {email_match.group()}")
    else:
        print("email is not found")    

if __name__ == "__main__":
    chapter1_basic()