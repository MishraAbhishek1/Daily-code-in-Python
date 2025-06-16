name = input("Enter your name : ")
# > without using strip method we did not remove a space simply we say a white space  ok bro >>
# print("your name is: ", {name})

# > this is inbulit python provide a strip method 
cleaned_name = name.strip()

print(f"your name is Beautiful : {cleaned_name}")