from datetime import datetime
class Employees():
    def __init__(self, name, last_name, birth_date):
            self.name = name
            self.last_name = last_name
            self.birth_year = birth_date
    def full_name(self):
          return f'{self.name} {self.last_name}'
    
    def employee_age(self):
          current_year = datetime.now().year
          age = int(current_year - self.birth_year)
          return age

user1 = Employees('Artur', 'Guimarães', 2002)
user2 = Employees('Elizabete', 'Guimarães', 1999)

# DENTRO DA CLASSE FUNCIONARIOS, TEM UMA FUNÇÃO (FULL NAME) QUE PRINTA AS INFO DO USER1
print(Employees.full_name(user1), Employees.employee_age(user1))
print(Employees.full_name(user2), Employees.employee_age(user2))