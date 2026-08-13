age = int (input ("Enter your age : "))

if age >= 18 : 
    print ("You are eligible to vote.")
else :
    print ("Sorry , you are too young to vote.")


marks = float (input ("Enter your exam marks :"))

if marks >= 80:
    print ("Grade : A+")
elif marks >= 70:
    print ("Grade : A")
elif marks >= 60:
    print ("Grade : A-")
elif marks >= 50:
    print ("Grade : B")
elif marks >= 33:
    print ("Grade : Pass")
else :
    print ("Grade : Fail")



has_nid = True
user_age = 20

if user_age >= 18 and has_nid == True:
    print ("You can open a bank account.")
else :
    print ("You cannot open a bank account.")

