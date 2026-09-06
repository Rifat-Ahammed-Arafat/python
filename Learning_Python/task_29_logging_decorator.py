"""টাস্ক: একটি ডেকোরেটর বানাও log_execution নামে। এটি যেকোনো ফাংশন চলার ঠিক আগে প্রিন্ট করবে: [LOG] Function is about to run... এবং ফাংশন শেষ হওয়ার পর প্রিন্ট করবে: [LOG] Function has finished.। একটি সাধারণ ফাংশনে এই ডেকোরেটর বসিয়ে কল করো।"""

def log_execution(func):
    def wrapper ():
        print ("[LOG] function is aobut to run...")
        func()
        print ("[LOG] Function has finished.")
    return wrapper

@log_execution
def greet_user():
    print ("Hello! Welcome to the application.")

greet_user()
