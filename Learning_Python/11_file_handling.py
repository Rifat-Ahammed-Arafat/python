with open ("my_notes.txt", "w") as file:
    file.write ("Line 1 : Learning python from scratch. \n")
    file.write("Line 2 : File handling is easy. \n")
print ("File created and written successfully.")

with open ("my_notes.txt", "a") as file:
    file.write("Line 3 : Appended a new line at the end. \n")
print ("New line added.")


print("\n--- Reading Full File ---")
with open ("my_notes.txt", "r") as file:
    content = file.read()
    print(content)