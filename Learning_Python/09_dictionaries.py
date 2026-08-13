student = {
    "name": "Rifat",
    "age": 24,
    "department": "Computer Science",
    "is_enrolled": True
}

print (f"Student name : {student["name"]}")
print (f"Department: {student.get("department")}")

student["age"] = 25
student["cgpa"] = 3.80

student.pop("is_enrolled")

print("\n--- Student Information ---")
for key , value in student.items():
    print ({key.capitalize(): {value}})