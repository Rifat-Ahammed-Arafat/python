my_list = []

for i in range (1, 6):
    num = int (input("Enter a number: "))
    my_list.append(num)
print (f"Full list: {my_list}")


print (f"Even numbers on the list : ")
for num in my_list:
    if num % 2 == 0 :
        print (num)
