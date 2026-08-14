try:
    with open("random_data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print ("File does not exist!")
finally:
    print ("Execution completed.")