students = ['Abhi', 'Ravi', 'Mona']
# print(enumerate(students))

for index, name in enumerate(students): # it starts deffault to 0
    print(index, name)

for index, name in enumerate(students, start=11):
    print(index, name)