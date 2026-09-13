def count_up_to (max_number):
    count = 1
    while count <= max_number:
        yield count
        count += 1


counter = count_up_to(3)

print (f"Step 1: {next(counter)}")
print (f"Step 2: {next(counter)}")
print (f"Step 3: {next(counter)}")


print("\n--- Looping through generator ---")
for number in count_up_to(5):
    print (number)
