try :
    num1 = int (input ("Enter numerator: "))
    num2 = int (input ("Enter denominator: "))

    result = num1 / num2
    print (f"Result : {result}")

except ZeroDivisionError:
    print ("[Error] you cannot divide a number by zero!")

finally :
    print ("Execution completed.")