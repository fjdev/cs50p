"""
WRITING IN ALL CAPS IS LIKE YELLING.
Best to use your “indoor voice” sometimes, writing entirely in lowercase.
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase.
Punctuation and whitespace should be outputted unchanged.
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
"""

# This main function gets the input from the user and calls the lower function to print the input in lowercase.
def main():
    sentence = input("")
    lower(sentence)

# This lower function takes the input variable 'text' from the user and prints it in lowercase.
def lower(text):
    print(text.lower())

main()
