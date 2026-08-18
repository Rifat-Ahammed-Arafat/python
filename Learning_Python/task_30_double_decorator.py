def double_result(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

final_output = add(5, 10)
print (f"Result after decorator: {final_output}")
