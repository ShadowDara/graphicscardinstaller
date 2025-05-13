# The Loading Message at the beginning of the app

# Better Debbuging
from rich.traceback import install
install()

import time
import sys

from rich import print
from rich.console import Console
from rich.markup import escape
from rich.text import Text

from app.vars import __version__
from app.vars import __alphabet__
from app.vars import __text_sleep__

console = Console()


def crazy_print_rich(markup: str):
    """
    Gibt Text Buchstabe für Buchstabe animiert mit Rich-Markup aus – ohne Zeilenumbruch.
    Beispiel-Markup: "[bold magenta]Hallo [underline blue]Welt[/][/]"
    """
    word = ""
    for char in markup:
        for _char_ in __alphabet__:
            sys.stdout.write('\r')  # Zeile zurücksetzen
            preview = word + _char_
            console.print(Text.from_markup(preview), end="", soft_wrap=True, highlight=False)
            sys.stdout.flush()
            time.sleep(__text_sleep__)
            if char == _char_:
                word += _char_
                break
            if _char_ == __alphabet__[-1] and char not in __alphabet__:
                word += char

def main():
    # The Text which will be printed in the Terminal!

    # Graphic Card Installer Version {__version__} made by Shadowdara
    crazy_print_rich(f"[bold magenta]Graphic Card Installer Version [underline blue]{__version__}[/] made by [underline blue]Shadowdara[/]      \n\n")

    # Starting the Software ...
    crazy_print_rich("[bold green]Starting the Software ...")

    print()
    print("[bold dark_orange]Achtung![/]")
    print("[on light_salmon black]Farbhintergrund + Textfarbe[/]")

if __name__ == "__main__":
    # For Faster Testing!
    __text_sleep__ = 0.001

    main()
