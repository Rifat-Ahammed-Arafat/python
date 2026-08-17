# ==========================================
# ১. List Comprehension
# ==========================================

squares = []
for i in range (1, 6):
    squares.append(i ** 2)
print (f"Regular loop squares: {squares}")  


squares_compact = [i ** 2 for i in range (1, 6)]
print (f"List comprehension squares: {squares_compact}")

even_numbers = [num for num in range (1, 11) if num % 2 == 0]
print (f"Even numbers : {even_numbers}")


# ==========================================
# ২. Lambda Function
# ==========================================

def add (a, b):
    return a + b

add_lambda = lambda a, b : a + b

print (f"sum using def : {add(10, 20)}")
print (f"sum using lambda : {add_lambda(10, 20)}")

double = lambda x : x * 2
print (f"Double of 5: {double(5)}")