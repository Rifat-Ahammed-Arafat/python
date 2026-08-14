class Employee :
    def __init__(self, name, salary):
        self. name = name 
        self.salary= salary

class Developer (Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_skills(self):
        print (f"{self.name} works using {self.programming_language}")


dev = Developer("Arafat", 200, "Python")
dev.show_skills()