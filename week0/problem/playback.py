"""
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.
In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
"""

# This main function gets the input from the user and calls the playback function to print the input with spaces replaced by '...'.
def main():
    sentence = input("")
    playback(sentence)

# This playback function takes the input variable 'text' from the user and prints it with spaces replaced by '...'.
def playback(text):
    print(text.replace(" ", "..."))

main()