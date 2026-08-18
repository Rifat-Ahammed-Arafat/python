def my_decorator(func):
    def wrapper():
        print("[System] Execution started...")
        func()
        print("[System] Execution completed successfully.\n")
    return wrapper

@my_decorator
def greet_user():
    print("Hello! Welcome to the application.")

@my_decorator
def run_backup():
    print("Backing up system data...")


greet_user()
run_backup()


def upppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@upppercase_decorator
def get_user_greeting(name):
    return f"welcome, {name}"

print (get_user_greeting("Arafat"))