"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise output No.
"""

def main():
    # Prompts the user for the answer to the Great Question of Life, the Universe and Everything.
    x = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

    # Converts the user input to lowercase to make it case-insensitively.
    x = x.lower()

    # Checks if the user input equals to 42 or forty-two or forty two.
    if x == "42" or x == "forty-two" or x == "forty two":
        print("Yes")
    else:
        print("No")

main()