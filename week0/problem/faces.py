"""
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face.
Nowadays, programs tend to convert emoticons to emoji automatically!
In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged.
Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
Be sure to call main at the bottom of your file.
"""

# This main function gets the input from the user and calls the convert function to print the input with :) converted to 🙂 and :( converted to 🙁.
def main():
    sentence = input("")
    convert(sentence)

# This convert function takes the input variable 'text' from the user and prints it with :) converted to 🙂 and :( converted to 🙁.
def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

main()