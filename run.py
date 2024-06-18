"""This Python code snippet is importing the `init`
function from the `colorama` module
and the `Menu` class from a module named `menu`."""

from colorama import init
from console.menu import Menu


if __name__ == "__main__":
    init(autoreset=True)
    menu = Menu()
    menu.run()
