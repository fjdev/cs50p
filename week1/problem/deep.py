"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise output No.
"""

def main():
    # Prompts the user for the answer to the Great Question of Life, the Universe and Everything.
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

    # Converts the user input to lowercase to make it case-insensitively and removes any leading or trailing spaces.
    answer = answer.lower().strip()

    # Checks if the user input equals to 42 or forty-two or forty two.
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()