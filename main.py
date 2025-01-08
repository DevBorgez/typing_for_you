import keyboard
import pyperclip
import time
import random

def on_hotkey():
    # Interval
    time.sleep(1)

    # Define the text you want to type
    text_to_type = """YOUR TEXT HERE"""

    # Main function to type text
    def fast_typing(text, delay_ascii=0.005):
        i = 0
        while i < len(text):
            try:
                char = text[i]
                if char.isascii():
                    keyboard.write(char, delay=delay_ascii)
                else:
                    pyperclip.copy(char)
                    keyboard.press_and_release('ctrl+v')
                    time.sleep(random.uniform(0.01, 0.03))
                i += 1
            except Exception as e:
                print(f"Error typing character: {e}")
                i += 1

    # Validates the input text before starting
    def validate_text(text):
        if not isinstance(text, str):
            raise ValueError("The text must be a string.")
        if len(text) == 0:
            raise ValueError("The text cannot be empty.")

    try:
        validate_text(text_to_type)
        fast_typing(text_to_type)
    except Exception as e:
        print(f"General error: {e}")

# Set up hotkey listener for Ctrl + Alt + ´
keyboard.add_hotkey('ctrl+alt+´', on_hotkey)

# Keep the program running
print("Press Ctrl + Alt + T to activate the hotkey...")
keyboard.wait('esc')  # Exits when ESC is pressed
