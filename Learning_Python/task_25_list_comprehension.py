"""টাস্ক: ১ থেকে ২০ পর্যন্ত সংখ্যার মধ্য থেকে শুধু বিজোর (Odd) সংখ্যাগুলোর বর্গ (Square) বের করে একটি নতুন লিস্টে রাখো। কাজটি সম্পূর্ণ করতে হবে List Comprehension ব্যবহার করে (কোনো সাধারণ for লুপ বা .append() ব্যবহার করা যাবে না)।"""

odd_squares = [num  ** 2 for num in range(1,25) if num % 2 != 0]

print (f"The list of squares of odd numbers: {odd_squares}")