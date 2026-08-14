numbers = []

for num in range (1,6):
    num = int (input(f"Enter a number {num}: "))
    numbers.append(num)
print (f"List: {numbers}")

unique_list = list(set(numbers))
print (f"Unique list (No Duplicates): {unique_list}")







