def calculate_square(number):
    square = number ** 2
    return  square

number = int(input("Enter a number: "))

squared_value = calculate_square(number)
print (f"Square of {number}: {squared_value}")
