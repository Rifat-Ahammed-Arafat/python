with open ("user_data.txt", "r") as file:
    content = file.read()
    total_characters = len(content)
    print (f"File content: \n{content}")
    print (f"Total characters in that file : {total_characters}")