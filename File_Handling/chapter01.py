'''
> using open function() perform these actions
     Mode	Description

        'r'	Read (default)
        'w'	Write (overwrite)
        'a'	Append
        'x'	Create file
        'b'	Binary mode
        't'	Text mode (default)
        'r+'	Read and Write
'''

# first we do open and read file
file = open('example.txt')
content = file.read()
print(content)
file.close