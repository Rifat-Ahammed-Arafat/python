"""টাস্ক: একটি প্যারেন্ট ক্লাস Employee বানাও যার ভেতর name এবং salary থাকবে।

একটি চাইল্ড ক্লাস Developer বানাও যা Employee কে ইনহেরিট করবে এবং এতে নতুন একটি অ্যাট্রিবিউট programming_language থাকবে।

Developer ক্লাসে একটি মেথড থাকবে show_skills() যা প্রিন্ট করবে: {name} works using {programming_language}।"""

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