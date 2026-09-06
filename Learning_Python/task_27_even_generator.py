"""টাস্ক: even_numbers(limit) নামে একটি Generator ফাংশন বানাও যা yield ব্যবহার করে $1$ থেকে $limit$ পর্যন্ত শুধু জোড় (Even) সংখ্যাগুলো এক এক করে প্রডিউস করবে। এরপর একটি for লুপ দিয়ে $limit = 10$ দিয়ে টেস্ট করো।"""

def even_numbers(limit):
     for i in range(1, limit+1):
          if i % 2 == 0:
               yield i


even = even_numbers(10)
print(f"step 1: {next(even)}")
print(f"step 2: {next(even)}")
print(f"step 3: {next(even)}")