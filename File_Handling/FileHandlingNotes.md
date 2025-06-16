> in a Python File Handling is a important part for a web applications //
> Python has several functions for creating, reading, updating, and deleting files.

🔰 1. Introduction to File Handling in Python
📘 Definition:
File handling ka matlab hota hai kisi file ko open, read, write, append, close karna Python ke through.

🔑 Built-in Function:
python
Copy
Edit
open()  # Used to open a file
📁 File Modes:
Mode	Description
'r'	Read (default)
'w'	Write (overwrite)
'a'	Append
'x'	Create file
'b'	Binary mode
't'	Text mode (default)
'r+'	Read and Write

🧱 2. Basic File Operations
✅ Open and Read File
python
Copy
Edit
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
✅ Read Line by Line
python
Copy
Edit
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
✍️ 3. Writing to Files
✅ Overwrite file content
python
Copy
Edit
with open('example.txt', 'w') as f:
    f.write("This will overwrite the content.")
✅ Append to file
python
Copy
Edit
with open('example.txt', 'a') as f:
    f.write("\nThis will be added at the end.")
📑 4. File Methods
python
Copy
Edit
f.read()        # Reads entire content
f.readline()    # Reads one line
f.readlines()   # Reads all lines in a list
f.write(str)    # Writes string to file
f.writelines(list)  # Writes list of strings
f.close()       # Closes the file
🔒 5. With Statement (Context Manager)
✅ Best practice to open files
python
Copy
Edit
with open('example.txt', 'r') as f:
    data = f.read()
# No need to close manually
📋 6. Working with File Paths
python
Copy
Edit
import os

print(os.getcwd())   # Current directory
os.chdir('path')     # Change directory
os.listdir()         # List files
💾 7. Check If File Exists
python
Copy
Edit
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")
🧠 8. Advance Reading/Writing Techniques
✅ Read/write specific number of characters
python
Copy
Edit
f.read(10)  # Read first 10 characters
✅ File pointer position
python
Copy
Edit
f.tell()    # Get current position
f.seek(0)   # Move pointer to start
🛠️ 9. Deleting & Renaming Files
python
Copy
Edit
import os

os.rename("old.txt", "new.txt")
os.remove("file.txt")
📂 10. Create and Delete Directories
python
Copy
Edit
os.mkdir("new_folder")        # Create single folder
os.makedirs("a/b/c")          # Create nested folders

os.rmdir("new_folder")        # Remove empty folder
os.removedirs("a/b/c")        # Remove nested folders
🧪 11. Working with JSON Files
python
Copy
Edit
import json

data = {"name": "Alpha", "age": 25}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON
with open("data.json", "r") as f:
    content = json.load(f)
    print(content)
📑 12. CSV File Handling
python
Copy
Edit
import csv

# Write CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alpha", 25])

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
🧰 13. Working with Binary Files
python
Copy
Edit
with open('binary_file.bin', 'wb') as f:
    f.write(b"This is binary data.")

with open('binary_file.bin', 'rb') as f:
    data = f.read()
    print(data)
🔐 14. Best Practices
Always use with open() for file operations.

Always check file existence before read/write.

Use try-except for error handling in file I/O.

Use modules like csv, json, pickle for structured data.

🎯 Real-World Mini Project Ideas
Expense Logger – Write/read expenses from text/CSV.

Student Report Card Generator – JSON-based record system.

Log Analyzer – Read server logs and extract info.

CV Parser – Read resumes from folder and extract info.

File Backup System – Copy important files to backup folder.