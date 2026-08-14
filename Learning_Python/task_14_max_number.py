def find_max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else: return a

a = int (input("Enter a number : "))
b = int (input("Enter another number : "))


max_value = find_max(a, b)
print (f"Max value is : {max_value}") 
    