print("--- For Loop Example ---")
for i in range (1,6):
    print (f"Number: {i}")


print("\n--- While Loop Example ---")
count = 1
while count <= 5:
    print (f"Count : {count}")
    count += 1


print("\n--- Break & Continue Example ---")
for num in range(1,10):
    if num == 3:
        continue
    if num == 7:
        break

    print (f"Corrent value : {num}")