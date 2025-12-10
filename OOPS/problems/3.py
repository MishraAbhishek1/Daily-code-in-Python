# Person class with age ke according kon se year me born hua hain

# now we solve a with taking input from users

from datetime import datetime

class Employee:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

     # here make a logcic behalf the  user fill age calculate the year
    def calculate_birth_year(self):
        current_year = datetime.now().year
        return current_year - self.age
        
p = Employee("abhishek", 21, "India")
birth_year = p.calculate_birth_year()
print(f"{p.name} was born in the year {birth_year}")