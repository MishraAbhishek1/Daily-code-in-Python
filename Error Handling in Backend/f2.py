# 2. File Handling (File Not Found)

try:
    with open("non_existent_file.txt", "r")as file:
        content = file.read()
        print(content)
except Exception as e:
    print("Error: ", e)        