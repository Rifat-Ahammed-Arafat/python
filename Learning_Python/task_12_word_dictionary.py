"""টাস্ক: ৩টি ইংরেজি শব্দ এবং তাদের বাংলা অর্থ দিয়ে একটি ডিকশনারি তৈরি করো।

(যেমন: words = {"apple": "আপেল", "book": "বই", "cat": "বিড়াল"})

ইউজার থেকে একটি ইংরেজি শব্দ ইনপুট নাও। যদি শব্দটি ডিকশনারিতে থাকে, তবে তার বাংলা অর্থ প্রিন্ট করো, আর না থাকলে প্রিন্ট করো Word not found!।"""

words = {"apple": "আপেল", "book": "বই", "cat": "বিড়াল"}

eng_word = input ("Enter an english word: ").lower()
if eng_word in words:
    print (f"Meaning: {words[eng_word]}")
else : 
    print ("Word not found!")