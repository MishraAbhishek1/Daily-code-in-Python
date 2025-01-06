# Check if a string is a Palindrome
""" problem: Determine if a given string reads the same backward as forward """
# string = "aba"
# print(string[::-1])
# print(string("aba"))
# print(string("baa"))
def is_palindrome(s):
    return s == s[::-1]
#Example
print(is_palindrome("radar"))
print(is_palindrome("hello"))

# str = "abacxe"
# if(str == str[::-1]):
#     print("Yes it is a Palindrome")

user_input = input("Enter Something: ")
print("You entered:", user_input)