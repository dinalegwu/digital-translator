print("WELCOME TO THE DIGITAL TRANSLATOR")

name = input("What is your name? ")
print("Hello", name)

word = input("Enter a word: ")
print("Your word is:", word)

choice = input("Choose upper or lower: ")

if choice == "upper":
    print(word.upper())
if choice == "lower":
    print(word.lower())
else:
    print("Invalid choice. Please choose upper or lower.")