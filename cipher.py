# add your code here
ab = ["a", "b", "c", "d", "e", "f", "g", "h" ,"i" ,"j", 
      "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
      "u", "v", "w", "x", "y", "z"]
sentence = input("enter a sentence: ")

code_words = sentence.split()


code_letters = ""
for word in code_words:
    for letter in word:
        code_letters += ab[(ab.index(letter) + 5) % 26]
    code_letters += " "
print(code_letters) 

#undo code
#code_sentence = input("Enter coded sentence: ")
#uncode_word = code_sentence.split()

#uncode_letters = ''
#for word in uncode_word:
    #for letter in word:
        #uncode_letters += ab[(ab.index(letter) - 5) % 26]
    #uncode_letters += " "
#print(uncode_letters)
