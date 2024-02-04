class Employee:
    def __init__(self, first, last, mail):
        self.first = first
        self.last = last
        self.mail = mail


emp1 = Employee('Maha', 'ElMorsy', 'mahaelmorsy92@gmail.com')
emp2 = Employee('Nada', 'Osman', 'nadaosman96@gmail.com')

# emp1.first = 'Maha'
# emp1.last = 'ElMorsy'
# emp1.mail = 'mahaelmorsy@gmail.com'
#
# emp2.first = 'Nada'
# emp2.last = 'Osman'
# emp2.mail = 'nadaosman@gmail.com'

print(emp1.mail)
print(emp2.mail)
