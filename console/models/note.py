"""
This module defines the Note class representing
a note with a title and content.
"""


class Note:
    """
    Represents a note with a title and content.
    """

    def __init__(self, title: str, content: str) -> None:
        """
        Initialize a Note instance with a title and content.

        Args:
            title (str): The title of the note.
            content (str): The content of the note.
        """
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        """
        Return a string representation of the Note object.

        Returns:
            str: String representation of the Note object, showing its title.
        """
        return f"Note: {self.title}"

    def display_info(self) -> str:
        """
        Display the title and content of the note.
        """
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
