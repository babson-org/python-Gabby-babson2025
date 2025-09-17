# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: Gabby Lopes
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
### START OF GABBY'S CODE PT. I
# While loop continuously prompts user to enter a valid number within the parameters (odd, int)
    while True:
        try:
            height = int(input("Enter an odd number: ")) # Ask user for diamond here
            if height % 2 == 1: # This verifies that the value entered is odd
                break # Once user enters a valid input, exits loop
            else:
                print("Error must enter an odd value, retry: ") # If an even value is entered
        except ValueError:
            print("Refer to directions and please try again") # If value is not an integer
    middle = height // 2 # This finds the middle index, determining spacing of diamond
    # Drawing the TOP half of the diamond, including the middle row
    for idx in range (middle, -1, -1): # Loops from middle down to zero
        before = " " * idx # These are the spaces before the first asteriks to center row
        between = " " * ((middle - idx) * 2 - 1) # Spaces between two asteriks
        if (middle - idx) * 2 - 1 == -1: # Because there is only one asteriks in this row
            print(before + "*")
        else:
            print(before + "*" + between + "*") # Prints asteriks with spaces in between
    # Drawing the BOTTOM half of the diamond (like code above but "reflected")
    for idx in range (1, middle + 1): # Loops from 1 up to middle
        before = " " * idx
        between = " " * ((middle - idx) * 2 -1)
        if (middle - idx) * 2 -1 == -1:
            print(before + "*")
        else:
            print(before + "*" + between + "*")
# Call the function to run drawing of diamond!
draw_diamond()
# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

### START OF GABBY'S CODE PT. II
# Have to ask user to input block of text
text = input("Enter some text: ")

# Counts letters as only alphabetical characters (a-z) or (A-Z)
letters = sum(1 for ch in text if ch.isalpha())

# Count words
# Want to split by text by whitespace in between and count the resulting
words = len(text.split())

# Counts sentences and punctuation as marked below in sentence endings
sentences = sum(text.count(end) for end in ".?!")

# Prints the results
print(f"Letters: {letters}")
print(f"Words: {0}")        # replace 0
print(f"Sentences: {0}")    # replace 0

# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
### START OF GABBY'S CODE PT.III
def caesar_cipher():
    # Function is running
    print("you have some work todo!, caesar_cypher")
    # Ask user for text that'll either be encrypted or decrypted later in function
    text = input("Enter text: ")
    # Continously ask user for shift value until given one within parameters (integer)
    while True:
        try:
            shift = int(input("Enter shift value as integer: "))
            break # This exits loop once the valid integer is provided by user input
        except ValueError:
            print("Error, please enter an integer") # Handles any invalid input
    # Prompts user whether they want to encrypt or decrypt
    while True:
        choice = input("Type 'e' to to encrypt or 'd' to decrypt: ").lower()
        if choice in ['e','d']:
            break # Valid choice is entered, either 'e' or 'd'
        else:
            print("Error, please type 'e' or 'd'") # Handles any invalid input
    # Creates a list of alphabet letters (a-z)
    alphabet = [chr(i) for i in range (97, 97 + 26)]
    # Create an empty string to later build the output
    result = " "
    for char in text:
        if char.isalpha(): # So it only processes letters
            is_upper = char.isupper() # Remembers if original character was uppercase
            index = alphabet.index(char.lower()) # Identifies index within alphabet
            if choice == 'e': # Will encrypt --> Shift forwards
                shifted_index = (index + shift) % 26 # Wraps around using modulus 
            else: # Will decrypt --> Shift backwards
                shifted_index = (index - shift) % 26
            new_char = alphabet[shifted_index] # Gets the new letter
            result += new_char.upper() if is_upper else new_char # Preserves case from original
        else:
            result += char # Characters that aren't letters remain as they were
    print("Result:", result)
    
caesar_cipher()




if __name__ == "__main__":
    main()