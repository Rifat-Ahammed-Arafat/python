coordinates = (10, 20, 30)

print (f"X coordinate: {coordinates[0]}")
print (f"Y coordinate: {coordinates[1]}")



numbers_set = {1,2,3,3,4,4,5}
print (f"Unique set items: {numbers_set}")

numbers_set.add(6)
numbers_set.remove(1)
print (f"Updated set: {numbers_set}")

raw_list = [10,20,20,30,40,40,50]
clean_list = list(set(raw_list))
print(f"List without duplicates: {clean_list}")
