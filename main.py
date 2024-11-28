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

def place_ships(field):
    ships = [(3,1), (2,2), (1,4)]
    for size, count in ships:
        for _ in range(count):
            while True:
                x = random.randint(0,6)
                y = random.randint(0, 6)
                direction = random.choice(["Horizontal", "Vertical"])
                if can_be_placed(field,x, y, size, direction):
                    place_ship(field,x, y, size, direction)
                    break

def can_be_placed(field, x, y, size, direction):
    for _ in range(size):
        if direction == "Vertical":
            nx, ny = x + 1, y
        else:
            nx, ny = x, y + 1
        if not (0 < nx < 7 and 0 < ny < 7) or (field[nx][ny] != " "):
            return False
        else:
            return True

def place_ship(field, x, y, size, direction):
    for _ in range(size):
        if direction == "Vertical":
            nx, ny = x + 1, y
        else:
            nx, ny = x, y + 1
        field[nx][ny] = "[S]"

print(random.choice(["Horizontal", "Vertical"]))