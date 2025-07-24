# 🔹7. Count Vowels in String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0

    for char_match in s:
        if char_match in vowels:
            count += 1
    return count
print(count_vowels("Abhishek"))    