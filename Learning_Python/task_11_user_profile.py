name = input ("Enter your name : ")
city = input ("Enter your city: ")
fav_subject = input ("Enter your favourite subject: ")

information = {
    "name" : name,
    "city" : city,
    "fav_subject" : fav_subject
}

for key , value in information.items():
    print (f"{key.capitalize()}: {value}")