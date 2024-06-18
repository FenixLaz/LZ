"""
This module implements a Menu class for interacting
with a note-taking application.
"""
from colorama import Fore, Style
from .database.db import Database
from .models.note import Note
from .utils.utils import clear_console, print_header, get_valid_note_id


class Menu:
    """
    Menu class provides methods to display menu options and interact with
    a note-taking application.
    """

    def __init__(self) -> Database:
        """
        Initialize Menu instance with a Database instance.
        """
        self.db = Database()

    def run(self) -> str:
        """
        Run the main menu loop until the user chooses to exit.
        """
        while True:
            clear_console()
            self.display_main_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_note_menu()
            elif choice == "2":
                self.view_notes_menu()
            elif choice == "3":
                self.search_notes_menu()
            elif choice == "4":
                self.delete_note_menu()
            elif choice == "5":
                self.exit_menu()
                break
            else:
                self.invalid_choice()

    def display_main_menu(self) -> str:
        """
        Display the main menu options.
        """
        print_header("Меню", Fore.CYAN + Style.BRIGHT)
        print("1. Добавить новую заметку")
        print("2. Просмотреть все заметки")
        print("3. Поиск заметок")
        print("4. Удалить заметку")
        print("5. Выйти")
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def add_note_menu(self) -> str:
        """
        Prompt user to input title and content for a new note
        and add it to the database.
        """
        clear_console()
        print_header("Добавить новую заметку", Fore.CYAN + Style.BRIGHT)
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержание заметки: ")
        note = Note(title, content)
        self.db.add_note(note)
        print(Fore.GREEN + "Заметка добавлена.")
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")

    def view_notes_menu(self) -> str:
        """
        Display all notes stored in the database and allow
        user to view details of a specific note.
        """
        clear_console()
        print_header("Список всех заметок", Fore.CYAN + Style.BRIGHT)
        notes = self.db.get_all_notes()
        if notes:
            for note in notes:
                print(Fore.CYAN + f"{note[0]}. {note[1]}")
            note_id = get_valid_note_id(
                "Введите ID заметки для подробного "
                "просмотра или 0, чтобы выйти: "
            )
            if note_id == 0:
                return
            if note_id is not None:
                self.display_note_details(note_id)
        else:
            print(Fore.RED + "Заметок нет.")
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")

    def display_note_details(self, note_id: int) -> str:
        """
        Display details (title and content) of a specific note by its ID.
        """
        note = self.db.get_note_by_id(note_id)
        if note:
            clear_console()
            print(Fore.CYAN + "=" * 50)
            print(Fore.CYAN + f"Заголовок: {note[1]}")
            print(Fore.CYAN + f"Содержание: {note[2]}")
            print(Fore.CYAN + "=" * 50)
        else:
            print(Fore.RED + "Заметка не найдена.")

    def search_notes_menu(self) -> str:
        """
        Prompt user to input a keyword for searching notes by title or content.
        Display matching notes found in the database.
        """
        clear_console()
        print_header("Поиск заметок", Fore.CYAN + Style.BRIGHT)
        notes_all = self.db.get_all_notes()
        if notes_all:
            keyword = input("Введите ключевое слово для поиска: ")
            notes = self.db.search_notes(keyword)
            if notes:
                for note in notes:
                    print(Fore.CYAN + f"{note[0]}. {note[1]}")
            else:
                print(Fore.RED + "Заметки не найдены.")
        else:
            print(Fore.RED + "База заметок пуста.")
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")

    def delete_note_menu(self) -> str:
        """
        Display all notes stored in the database
        and allow user to delete a specific note by its ID.
        """
        clear_console()
        print_header("Удалить заметку", Fore.CYAN + Style.BRIGHT)
        notes = self.db.get_all_notes()
        if notes:
            for note in notes:
                print(Fore.CYAN + f"{note[0]}. {note[1]}")
            note_id = get_valid_note_id(
                "Введите ID заметки для удаления"
                " или 0, чтобы выйти: "
            )
            if note_id == 0:
                return
            if note_id is not None:
                self.delete_note_by_id(note_id)
        else:
            print(Fore.RED + "Заметок ещё нет.")
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")

    def delete_note_by_id(self, note_id: int) -> str:
        """
        Delete a specific note by its ID from the database.
        """
        note = self.db.get_note_by_id(note_id)
        if note:
            self.db.delete_note_by_id(note_id)
            print(Fore.GREEN + "Заметка удалена.")
        else:
            print(Fore.RED + "Заметка с таким ID не найдена.")

    def exit_menu(self) -> str:
        """
        Close the database connection and exit the application.
        """
        clear_console()
        self.db.close()
        print(Fore.RED + "База данных закрыта.")
        print(Fore.RED + "Вы вышли из программы.")

    def invalid_choice(self) -> str:
        """
        Display a message when the user
        makes an invalid choice in the main menu.
        """
        print(Fore.RED + "Неверный выбор, попробуйте снова.")
        input(Fore.YELLOW + "Нажмите Enter, чтобы продолжить...")
