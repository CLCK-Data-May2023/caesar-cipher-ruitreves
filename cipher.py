ab = ["a", "b", "c", "d", "e", "f", "g", "h" ,"i" ,"j", 
      "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
      "u", "v", "w", "x", "y", "z"]
sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

code_words = sentence.split()


code_letters = ""
for word in code_words:
    for letter in word:
        if letter in ab:
            code_letters += ab[(ab.index(letter) + 5) % 26]
        else: 
            code_letters += letter
    code_letters += " "
print("The encrypted sentence is:", code_letters) 
#
