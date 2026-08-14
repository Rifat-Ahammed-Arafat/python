try :
    num = int (input ("Enter an integer: "))
    print (f"The integer is : {num}")
except ValueError:
    print ("Please enter a valid integer!")
finally :
    print ("Execution completed.")