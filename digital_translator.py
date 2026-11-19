print("WELCOME TO THE DIGITAL TRANSLATOR")

name = input("What is your name? ")
print("Hello", name)

word = input("Enter a word: ")
print("Your word is:", word)

choice = input("Choose upper or lower: ").strip().lower()

if choice == "upper":
    print(word.upper())
elif choice == "lower":
    print(word.lower())
elif choice == "title":
    print(word.title())
else:
    print("Invalid choice. Please choose upper or lower.")