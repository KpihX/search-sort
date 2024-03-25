#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import sys

# Define a type alias for clarity, 'real' represents numerical types int or float
real = int | float

# Message to display when the program is about to stop
stop_message = "Une saisie vide interrompt le programme"

def bye() -> None:
    """
    Displays a farewell message and exits the program.
    
    Time Complexity: O(1), as it performs a constant number of operations.
    Space Complexity: O(1), as it does not allocate any additional space.
    """
    input("\nRavi de vous avoir servi! Pressez 'Entrer' pour quitter.")
    sys.exit()

def control_exit(value: str) -> None:
    """
    Checks if the provided value is an empty string and triggers program exit.
    
    Parameters:
    value (str): The string to check for emptiness.
    
    Time Complexity: O(1), as it checks a single condition.
    Space Complexity: O(1), as it uses no extra space.
    
    Returns:
    None: This function does not return a value; it exits the program if the condition is met.
    """
    if value == '':
        bye()

if __name__ == "__main__":
    import utils
    print(help(utils))