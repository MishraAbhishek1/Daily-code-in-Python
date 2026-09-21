s = "Hello World"

# How i count last word i know after space i count 

count = 0
for i in s[::-1]:
    if i == ' ':
       break
    count += 1
    # print(i)

print(count)