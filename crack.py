"""
Step 3: Decipher the Text
    based on the assumption the following are the most common characters in English in this order:
    ETAOINSHRDL

    Letter frequency order gotten from:https://en.wikipedia.org/wiki/Letter_frequency

    Using python turtle for GUI
"""
#!/usr/bin/env python3
import turtle
import sys
import frqanal
import os
import string

# Function to create a pop-up window and get user input
def get_user_input(prompt):
    user_input = turtle.textinput("Cipher Decipher", prompt)
    return user_input

"""
Step 3: Decipher the Text
    based on the assumption the following are the most common characters in English in this order:
    ETAOINSHRDL

    Letter frequency order gotten from:https://en.wikipedia.org/wiki/Letter_frequency

    Using python turtle for GUI
"""
#!/usr/bin/env python3
import turtle
import sys
import frqanal
import os
import string

# Function to create a pop-up window and get user input
def get_user_input(prompt):
    user_input = turtle.textinput("Cipher Decipher", prompt)
    return user_input

# Function to display mappings on both Turtle window and command line
def display_mappings(mapping):
    mappings_str = "\n".join([f"{cipher} -> {plain}" for cipher, plain in mapping.items()])
    display_text(mappings_str, position=(10, -300))

# Function to display letter frequencies
def display_frequencies(frq):
    freq_str = "\n".join(frq)
    display_text(freq_str, position=(-200, -200))

# Function to display text on Turtle window
def display_text(text, position):
    turtle.penup()
    turtle.goto(position)
    turtle.write(text, align="left", font=("Arial", 12, "normal"))



# Main function
def main():
    # Initialize Turtle
    screen = turtle.Screen()
    screen.title("Cipher Decipher")

    # Get file name from user assuming all test ciphers are in the directory 'testciphers'
    file_name = get_user_input("Enter cipher text from /testciphers:")
    file_path = f"testciphers/{file_name}"  

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        turtle.bye()
        sys.exit()

    # Read the content of the file
    text = ''
    with open(file_path, 'r') as file:
        text = file.read()


    # Calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(text)
    frq = frqanal.sortedFreq(char_dict)
    turtle.penup()
    turtle.goto(-200, 200)  # Adjusted position
    display_frequencies(frq)

    mapping = {}
    invMapping = {}
    inp = ""

    # Get user input for number of letters to replace
    while not inp.isnumeric() or inp == "" or int(inp) > 26:
        inp = get_user_input("Input how many letters to replace in the cipher (1-26)")
    inp = int(inp)

    # Obtain mappings from user input
    for i in range(inp):
        letter = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'[i]
        cipherL = frq[i][0]
        mapping[cipherL] = letter
        invMapping[letter] = cipherL

    # Display mappings
    turtle.penup()
    turtle.goto(-200, -200)
    display_mappings(mapping)

    # Prompt user for next action
    while True:
        action = get_user_input("What would you like to do now?\n(1) New Mapping\n(2) Show Mappings\n(3) Done")
        if action == "3":
            turtle.bye()
            sys.exit()
        elif action == "2":
            turtle.clear()
            turtle.penup()
            turtle.goto(-200, -200)
            display_mappings(mapping)
        elif action == "1":
            # Prompt user for cipher character and replacement character
            cipher_char = get_user_input("What cipher character are you replacing?")
            if not cipher_char:
                continue  # If user cancels input, skip to next iteration
            replacement_char = get_user_input("What character should it be replaced with?")
            if not replacement_char:
                continue  # If user cancels input, skip to next iteration

            # Confirm mapping | ensure that there is a one to one replacement
            confirm = get_user_input(f'Type (Y) to add mapping "{cipher_char} -> {replacement_char}"')
            if confirm == "Y":
                if cipher_char in mapping:
                    if replacement_char in invMapping:
                        mapping[invMapping[replacement_char]] = mapping[cipher_char]
                        mapping[cipher_char] = replacement_char
                        invMapping = {v: k for k, v in mapping.items()}
                    else:
                        mapping[cipher_char] = replacement_char
                        invMapping = {v: k for k, v in mapping.items()}
                else:
                    if replacement_char in invMapping:
                        invMapping[replacement_char] = cipher_char
                        mapping = {v: k for k, v in invMapping.items()}
                    else:
                        mapping[cipher_char] = replacement_char
                        invMapping[replacement_char] = cipher_char

                turtle.clear()
                turtle.penup()
                turtle.goto(-200, -200)
                display_mappings(mapping)
                turtle.write("Added Mapping", align="left", font=("Arial", 12, "normal"))
    turtle.mainloop()

if __name__ == '__main__':
    main()


# Function to display letter frequencies
def display_frequencies(frq):
    freq_str = "\n".join(frq)
    turtle.hideturtle()
    turtle.goto(-200, -200)  
    turtle.write(freq_str, align="right", font=("Arial", 12, "normal"))
    print(freq_str)


# Main function
def main():
    # Initialize Turtle
    screen = turtle.Screen()
    screen.title("Cipher Decipher")

    # Get file name from user assuming all test ciphers are in the directory 'testciphers'
    file_name = get_user_input("Enter cipher text from /testciphers:")
    file_path = f"testciphers/{file_name}"  

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        turtle.bye()
        sys.exit()

    # Read the content of the file
    text = ''
    with open(file_path, 'r') as file:
        text = file.read()


    # Calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(text)
    frq = frqanal.sortedFreq(char_dict)
    turtle.penup()
    turtle.goto(-200, 200)  # Adjusted position
    display_frequencies(frq)

    mapping = {}
    invMapping = {}
    inp = ""

    # Get user input for number of letters to replace
    while not inp.isnumeric() or inp == "" or int(inp) > 26:
        inp = get_user_input("Input how many letters to replace in the cipher (1-26)")
    inp = int(inp)

    # Obtain mappings from user input
    for i in range(inp):
        letter = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'[i]
        cipherL = frq[i][0]
        mapping[cipherL] = letter
        invMapping[letter] = cipherL

    # Display mappings
    turtle.penup()
    turtle.goto(-200, -200)
    display_mappings(mapping)

    # Prompt user for next action
    while True:
        action = get_user_input("What would you like to do now?\n(1) New Mapping\n(2) Show Mappings\n(3) Done")
        if action == "3":
            turtle.bye()
            sys.exit()
        elif action == "2":
            turtle.clear()
            turtle.penup()
            turtle.goto(-200, -200)
            display_mappings(mapping)
        elif action == "1":
            # Prompt user for cipher character and replacement character
            cipher_char = get_user_input("What cipher character are you replacing?")
            if not cipher_char:
                continue  # If user cancels input, skip to next iteration
            replacement_char = get_user_input("What character should it be replaced with?")
            if not replacement_char:
                continue  # If user cancels input, skip to next iteration

            # Confirm mapping | ensure that there is a one to one replacement
            confirm = get_user_input(f'Type (Y) to add mapping "{cipher_char} -> {replacement_char}"')
            if confirm == "Y":
                if cipher_char in mapping:
                    if replacement_char in invMapping:
                        mapping[invMapping[replacement_char]] = mapping[cipher_char]
                        mapping[cipher_char] = replacement_char
                        invMapping = {v: k for k, v in mapping.items()}
                    else:
                        mapping[cipher_char] = replacement_char
                        invMapping = {v: k for k, v in mapping.items()}
                else:
                    if replacement_char in invMapping:
                        invMapping[replacement_char] = cipher_char
                        mapping = {v: k for k, v in invMapping.items()}
                    else:
                        mapping[cipher_char] = replacement_char
                        invMapping[replacement_char] = cipher_char

                turtle.clear()
                turtle.penup()
                turtle.goto(-200, -200)
                display_mappings(mapping)
                turtle.write("Added Mapping", align="left", font=("Arial", 12, "normal"))
    turtle.mainloop()

if __name__ == '__main__':
    main()
