def finding_letter_count(s):
    name = "Abhishek"
    count = 0

    for count_char in s:
        if count_char in name:
            count += 1
    return count        

print(finding_letter_count('h'))