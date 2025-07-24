# 🔹9. Check Palindrome

def check_palindrome(s):
    if s == s[::-1]:
          return f"{s} ==See this is  a Plaindrome =={s}"
    else:
         return "This is Not a Plaindrome"

print(check_palindrome("abacd"))     
     