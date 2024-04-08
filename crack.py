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

# Show content of the file using display_text
def display_file_content(text, position, chars_per_line):
    display_titles("Original Cipher Text", position=(-200, -150))
    lines = [text[i:i+chars_per_line] for i in range(0, len(text), chars_per_line)]
    formatted_text = '\n'.join(lines)
    display_text(formatted_text, position=(-290, -210))

# Screen to draw a line splitting the screen in half
def draw_split_line():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 300)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(400)
    turtle.penup()
    turtle.goto(-300, 260)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(600)

# Function to display titles on Turtle window
def display_titles(title, position):
    draw_split_line()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(position[0], position[1])
    turtle.write(title, align="center", font=("Arial", 20, "bold"))

# Display mappings 
def display_mappings(mapping, original_text):
    mappings_str = "\n".join([f"{cipher} -> {plain}" for cipher, plain in mapping.items()])
    display_titles("Mapping", position=(125, 270))
    display_text(mappings_str, position=(120, 30))
    print(mappings_str)

    # Print the original text with replacements
    print("Text Remapped:")
    replaced_text = replace_text(original_text, mapping)
    print(replaced_text)

    # Draw the replaced text on the screen below file content
    display_titles("Text Remapped", position=(-220, -245))
    display_replaced_text(replaced_text, position=(-275, -310), chars_per_line=75)

    return mappings_str

# Display letter frequencies
def display_frequencies(frq):
    freq_str = "\n".join(frq)
    display_titles("Frequency", position=(-155, 270))
    display_text(freq_str, position=(-200, 30))
    print(freq_str)

# Function to display top to bottom
def display_text(text, position, blue = False):
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
    if blue:
        turtle.color("blue")
        blue = False
    turtle.write('\n'.join(lines), align="left", font=("Arial", 12, "normal"))
    turtle.color("black")


# Function to replace text based on mapping
def replace_text(text, mapping):
    replaced_text = ""
    for char in text:
        replaced_text += mapping.get(char, char)
    return replaced_text

# Function to display the replaced text below file content
def display_replaced_text(text, position, chars_per_line):
    lines = [text[i:i+chars_per_line] for i in range(0, len(text), chars_per_line)]
    formatted_text = '\n'.join(lines)
    display_text(formatted_text,  position=(-290, -300), blue = True)

def main():
    # Initialize Turtle
    screen = turtle.Screen()
    screen.title("Cipher Decipher")
    draw_split_line()

    # Get file name from user assuming all test ciphers are in the directory 'testciphers'
    file_name = get_user_input("Enter cipher text from /testciphers:")
    file_path = f"testciphers/{file_name}"  

    # Check if the file exists and read and  the content of the file
    if not os.path.exists(file_path):
        print("File not found.")
        turtle.bye()
        sys.exit()
    text = ''
    with open(file_path, 'r') as file:
        text = file.read()
    display_file_content(text, position=(-275, -240), chars_per_line=75)

    # Calculate frequency of each letter in ciphertext
    char_dict = frqanal.charAnalysis(text)
    frq = frqanal.sortedFreq(char_dict)
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
    display_mappings(mapping, text)

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
                frq_str = display_frequencies(frqanal.sortedFreq(char_dict))
                display_mappings(mapping, text)
                display_file_content(text, position=(-275, -240), chars_per_line=75)

if __name__ == '__main__':
    main()
