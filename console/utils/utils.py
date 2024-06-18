"""
Modules that provide utility functions for console
operations and color formatting.
"""

import os
from colorama import Fore


def clear_console() -> None:
    """
    Clears the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def print_header(header: str, color: str) -> str:
    """
    Prints a formatted header with a specified color.

    Args:
        header (str): The header text to display.
        color (str): The color to use for printing (e.g., Fore.CYAN, Fore.RED).
    """
    print(color + "=" * 50)
    print(color + header.center(50))
    print(color + "=" * 50)


def get_valid_note_id(prompt: str) -> str:
    """
    Prompts the user for a valid note ID.

    Keeps prompting until the user enters a positive integer ID.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        int: The valid note ID entered by the user.
    """
    while True:
        try:
            note_id = int(input(Fore.CYAN + prompt))
            if note_id >= 0:
                return note_id
            print(Fore.RED + "ID должен быть положительным числом.")
        except ValueError:
            print(
                Fore.RED +
                "Некорректный ввод. Пожалуйста, введите числовой ID."
            )
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")
