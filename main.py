# Graphic Card Installer
# by Shadowdara
# Licensed under Apache License 2.0
# https://github.com/ShadowDara/graphicscardinstaller

# Better Debbuging
from rich.traceback import install
install()

import app.terminal_load as l
import app.start_ui as ui

def main():
    l.main()
    ui.main()

if __name__ == "__main__":
    main()
