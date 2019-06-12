#
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello_func(self):
        print('Hello my name is: ' + self.name)


p1 = Person('Little White', 3)
#   p1.name = 'Little Big'
#   print(p1.name)
#   del p1.name
#   del p1 <-- deleta o objeto

p1.hello_func()