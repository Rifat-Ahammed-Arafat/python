words = {"apple": "আপেল", "book": "বই", "cat": "বিড়াল"}

eng_word = input ("Enter an english word: ").lower()
if eng_word in words:
    print (f"Meaning: {words[eng_word]}")
else : 
    print ("Word not found!")