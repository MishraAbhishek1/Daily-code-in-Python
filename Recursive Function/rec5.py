# 🔹 Problem 2: Reverse a String

# string = "Hello"
# print(string[: :-1])

# BUt we dont do this likely

def reverse_string(s):

    # base case
    if len(s) == 0:
        return s
    
    # recursive case
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))