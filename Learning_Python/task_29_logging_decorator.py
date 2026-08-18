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
