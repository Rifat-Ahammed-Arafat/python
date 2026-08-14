class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def introduce(self):
        print (f"Hello, I am {self.name} and I am {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print (f"{self.name}'s Student ID is: {self.student_id} ")

p1 = Person("Rifat", 25)
p1.introduce()

s1 = Student("Arafat", 24 , 48547)
s1.introduce()
s1.show_id()