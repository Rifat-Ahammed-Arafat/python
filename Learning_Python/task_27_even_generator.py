def even_numbers(limit):
     for i in range(1, limit+1):
          if i % 2 == 0:
               yield i


even = even_numbers(10)
print(f"step 1: {next(even)}")
print(f"step 2: {next(even)}")
print(f"step 3: {next(even)}")