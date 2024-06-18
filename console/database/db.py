"""
Module to interact with the database for managing notes.
"""

import sqlite3
from ..models.note import Note


class Database:
    """
    Represents a SQLite database manager for notes.
    """

    def __init__(self, db_file: str = "notes.db") -> None:
        """
        Initialize the Database object.

        Args:
            db_file (str): Optional. The filename of the SQLite database.
        """
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self) -> None:
        """
        Create the 'notes' table if it does not exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_note(self, note: Note) -> None:
        """
        Add a new note to the database.

        Args:
            note (Note): The Note object to add to the database.
        """
        query = "INSERT INTO notes (title, content) VALUES (?, ?);"
        self.conn.execute(query, (note.title, note.content))
        self.conn.commit()

    def get_all_notes(self) -> list:
        """
        Retrieve all notes from the database.

        Returns:
            list: A list of tuples containing (id, title, content)
            for each note.
        """
        query = "SELECT id, title, content FROM notes;"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_note_by_id(self, note_id: int) -> list:
        """
        Retrieve a note from the database by its ID.

        Args:
            note_id (int): The ID of the note to retrieve.

        Returns:
            tuple or None: A tuple containing (id, title, content)
            of the note if found,
                None if no note found with the given ID.
        """
        query = "SELECT id, title, content FROM notes WHERE id = ?;"
        cursor = self.conn.execute(query, (note_id,))
        return cursor.fetchone()

    def search_notes(self, keyword: str) -> list:
        """
        Search for notes in the database by keyword in title or content.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of tuples containing (id, title)
            of notes matching the keyword.
        """
        query = """
            SELECT id, title
            FROM notes
            WHERE title LIKE ? OR content LIKE ?;
        """

        cursor = self.conn.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()

    def delete_note_by_id(self, note_id: int) -> list:
        """
        Delete a note from the database by its ID.

        Args:
            note_id (int): The ID of the note to delete.
        """
        query = "DELETE FROM notes WHERE id = ?;"
        self.conn.execute(query, (note_id,))
        self.conn.commit()

    def close(self):
        """
        Close the connection to the database.
        """
        self.conn.close()
