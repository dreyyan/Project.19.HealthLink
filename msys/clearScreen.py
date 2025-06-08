import os
# UTILITY: clear the console screen
def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")