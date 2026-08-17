num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
mul = lambda num1 , num2 : num1 * num2

print (f"Multiplication is : {mul(num1, num2)}")


string = input ("Enter a string: ")
string_len = lambda string : len(string)


print (f"String length is : {string_len(string)}")