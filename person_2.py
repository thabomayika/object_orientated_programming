class Person:
    # create a instance to  
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old. My interests are {self.interests}'
person = Person('Ryan', 30, 'male', f'being a hardarse agile and ssd hard drive')
greeting = person.hello()
print(greeting)
