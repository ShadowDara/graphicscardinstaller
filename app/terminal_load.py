# The Loading Message at the beginning of the app

# Better Debbuging
from rich.traceback import install
install()

import time
import sys
import random

from rich import print
from rich.console import Console
from rich.markup import escape
from rich.text import Text
from rich.progress import track

from app.vars import __version__
from app.vars import __alphabet__
from app.vars import __text_sleep__
from app.vars import __modules__
from app.vars import __module_time__

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
    """
    # Graphic Card Installer Version {__version__} made by Shadowdara
    crazy_print_rich(f"[bold magenta]Graphic Card Installer Version [underline blue]{__version__}[/] made by [underline blue]Shadowdara[/]      ")
    print("\n")

    # Starting the Software ...
    crazy_print_rich("[bold green]Starting the Software ...  ")
    print("\n\n")

    # Checking for Updates
    crazy_print_rich("[bold dark_orange]Checking for Updates")
    print("\n")

    # Updates available!
    crazy_print_rich("[bold red]Updates available!")
    print("\n\n")
    
    # Downloading the latest Version
    for task in track(range(100), description="[bold green]Downloading latest Version "):
        time.sleep(0.05)
    print("")

    # Installing the latest Version
    for task in track(range(100), description="[bold green]Installing latest Version  "):
        time.sleep(0.25)
    print("\n")
    
    # Intialiting
    for task in track(range(100), description="Intialising                "):
        time.sleep(1)
    print("\n")
    
    # Downlading Modules
    for task in track(range(100), description="[bold green]Downlading Modules         "):
        time.sleep(0.1)
    print("")

    # Installing Modules
    for task in track(range(100), description="[bold green]Installing Modules         "):
        time.sleep(0.1)
    print("")
    """
    # Checking Modules
    crazy_print_rich("[bold green]Checking the Modules")
    print("\n")

    # Printing all Modules
    for x in __modules__:
        print(f"{x} [bold green]Loaded![/]")
        time.sleep(2 / random.randint(1, __module_time__))
    print("")
    
    # All Modules are loaded succesfully!
    crazy_print_rich("[bold green]All Modules are loaded succesfully!")
    print("")


    #print("[bold dark_orange]Achtung![/]")
    #print("[on light_salmon black]Farbhintergrund + Textfarbe[/]")
