fruits = ["apple", "banana", "cherry", "orange"]

print ("First fruit: ", fruits[0])
print ("Last frutit: ", fruits[-1])

fruits[1] = "mango"
print ("Updated list : ", fruits)

fruits.append("grape")
fruits.insert(1, "berry")
print ("After addding items: ", fruits)

# fruits.remove("apple")
popped_item = fruits.pop()
print (f"Removed item : {popped_item}")
print (f"Current list: {fruits}")

print("\n--- Fruit List Items ---")
for fruit in fruits:
    print (f"I like {fruit}")