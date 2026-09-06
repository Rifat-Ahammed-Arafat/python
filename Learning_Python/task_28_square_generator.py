"""টাস্ক: square_sequence(n) নামে একটি Generator ফাংশন বানাও যা $1$ থেকে $n$ পর্যন্ত প্রতিটি সংখ্যার বর্গ ($x^2$) yield করবে। next() ফাংশন ৩ বার কল করে প্রথম ৩টি সংখ্যার বর্গ প্রিন্ট করে দেখাও।"""

def square_sequence(n):
    for i in range (1,n):
        i = i ** 2
        yield i

sq = square_sequence(10)
print (f"Step 1 : {next(sq)}")
print (f"Step 2 : {next(sq)}")
print (f"Step 3 : {next(sq)}")
