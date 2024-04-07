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

# Pop-up window and get user input
def get_user_input(prompt):
    user_input = turtle.textinput("Cipher Decipher", prompt)
    return user_input

# Screen to draw a line splitting the screen in half
def draw_split_line():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 300)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(600)

# Function to display titles on Turtle window
def display_titles(title, position):
    draw_split_line()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(position[0], position[1])
    turtle.write(title, align="center", font=("Arial", 20, "bold"))

# Display mappings 
def display_mappings(mapping):
    mappings_str = "\n".join([f"{cipher} -> {plain}" for cipher, plain in mapping.items()])
    display_titles("Mapping", position=(125, 200))
    display_text(mappings_str, position=(125, -50))
    print(mappings_str)

# Display letter frequencies
def display_frequencies(frq):
    freq_str = "\n".join(frq)
    display_titles("Frequency", position=(-200, 200))
    display_text(freq_str, position=(-200, -50))
    print(freq_str)

# Function to display text on Turtle window
def display_text(text, position):
    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
    lines = text.split('\n')
    
    # Calculate total height of text
    total_height = 12 * len(lines)
    content_position = (position[0], position[1] + total_height // 2)
    
    # Adjust for drawing from top to bottom
    content_position = (content_position[0], content_position[1] - 12 * (len(lines) - 1))
    
    turtle.goto(content_position[0], content_position[1])
    turtle.write('\n'.join(lines), align="left", font=("Arial", 12, "normal"))

def main():
    # Initialize Turtle
    screen = turtle.Screen()
    screen.title("Cipher Decipher")
    draw_split_line()

    # Get file name from user assuming all test ciphers are in the directory 'testciphers'
    file_name = get_user_input("Enter cipher text from /testciphers:")
    file_path = f"testciphers/{file_name}"  

    # Check if the file exists and read the content of the file
    if not os.path.exists(file_path):
        print("File not found.")
        turtle.bye()
        sys.exit()
    text = ''
    with open(file_path, 'r') as file:
        text = file.read()

    # Calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(text)
    frq = frqanal.sortedFreq(char_dict)
    turtle.penup()
    turtle.goto(-200, 200)
    display_frequencies(frq)

    mapping = {}
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

    # Display mappings
    turtle.penup()
    turtle.goto(-200, -200)
    display_mappings(mapping)

    # Prompt user for next action
    while True:
        action = get_user_input("What would you like to do now?\n(1) New Mapping\n(2) Done")
        if action == "2":
            turtle.bye()
            sys.exit()
        elif action == "1":
            # Prompt user for cipher character and replacement character
            cipher_char = get_user_input("What cipher character are you replacing?")
            if not cipher_char:
                continue  
            replacement_char = get_user_input("What character should it be replaced with?")
            if not replacement_char:
                continue  

            # Confirm mapping | ensure that there is a one to one replacement
            confirm = get_user_input(f'Type (Y) to add mapping "{cipher_char} -> {replacement_char}"')
            if confirm == "Y":
                mapping[cipher_char] = replacement_char
                turtle.clear()
                turtle.penup()
                turtle.goto(-200, -200)
                display_mappings(mapping)
                display_frequencies(frq)
    turtle.mainloop()

if __name__ == '__main__':
    main()
