# 🔹3. Find Even or Odd

def even_odd_finder(n):
    if n > 0:
        if n%2 == 0:
            print("This Number is Even")
        else:
            print("this number is Odd") 
    else:
        print("Please enter a Positive Number")  

result = even_odd_finder(-1)
print(result)        