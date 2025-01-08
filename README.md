# typing_for_you

# A fast typing automation script:

This script automates the typing of a predefined text when a specific keyboard shortcut is pressed.

## Features
- Types out text character by character, simulating manual typing.
- Supports special characters and non-ASCII text using clipboard paste.
- Allows for a customizable hotkey.

## How to Use
1. Install the keyboard library:
   	pip install keyboard
   
Run the script:
	python /path/to/main.py

## Customization
- Modify the `text_to_type` variable to change the text to be typed.
- Press Ctrl + Alt + ´ to activate the automation

## Limitations
- Requires admin permissions to listen for global hotkeys on some systems.
- Does not handle complex GUI interactions like mouse movements or advanced text fields.
