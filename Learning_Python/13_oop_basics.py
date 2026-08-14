class Student:
    def __init__(self, name , department, roll):
        self.name = name
        self.department = department 
        self.roll = roll

    def display_info(self):
        print(f"Student: {self.name} | {self.department} | {self.roll}")
    def study(self, subject):
        print (f"{self.name} is currently studying {subject}")

student1 = Student("Rifat", "Computer science", 101)
student2 = Student("Rahim", "Electrical", 102)

student1.display_info()
student1.study("Python OOP")

student2.display_info()