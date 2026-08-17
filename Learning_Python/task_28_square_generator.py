def square_sequence(n):
    for i in range (1,n):
        i = i ** 2
        yield i

sq = square_sequence(10)
print (f"Step 1 : {next(sq)}")
print (f"Step 2 : {next(sq)}")
print (f"Step 3 : {next(sq)}")
