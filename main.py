# git init
# git branch -M main
# git add .
# git commit -m init
# git remote add origin https://github.com/...
# git push -u origin main

# git add .
# git commit -m update
# git push
import random
import os
from dataclasses import field


# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_field(size = 7):
    return [[" " for _ in range(size)] for _ in range(size)]

def display_field(field, hidden = True):
    print("  " + "".join(str(i).center(3) for i in range(len(field))))
    for i, row in enumerate(field):
        if hidden:
            row_display = ["[ ]" if cell == "S" else f"[{cell}]" for cell in row]
        else:
            row_display = [f"[{cell}]" for cell in row]
        print(f"{i} " + ''.join(row_display))
print(display_field(create_field()))
