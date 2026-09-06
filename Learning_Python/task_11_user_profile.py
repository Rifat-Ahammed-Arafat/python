"""টাস্ক: ইউজার থেকে তার নাম (name), শহর (city) এবং প্রিয় বিষয় (fav_subject) ইনপুট নাও। এরপর এই ৩টি তথ্য দিয়ে একটি ডিকশনারি বানাও এবং লুপ চালিয়ে সব তথ্য প্রিন্ট করে দেখাও।"""

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