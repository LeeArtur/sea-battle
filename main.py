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
        field[nx][ny] = "S"

def player_shot():
    while True:
        shot = input("Enter coordinates of shot (separated by space): ").split()
        if len(shot) == 2 and (coordinate.isdigit() for coordinate in shot):
            row, col = map(int, shot)
            if 0 <= row <= 7 and 0 <= col <= 7:
                return row, col
        else:
            print("Invalid input. Try again")

def check_shot(field, x, y):
    if field[x][y] == "S":
        field[x][y] = "X"
        print("Hit!")
        return "Hit!"
    elif field[x][y] == " ":
        field[x][y] = "O"
        print("Miss!")
    else:
        print("You already hit there!")

def all_ship_sunk(field):
    for row in field:
        if "S" in row:
            return False
    return True

def gameplay():
    player_name = input("Enter your name: ")
    while True:
        field = create_field()
        place_ships(field)
        shots = 0
        while True:
            clear_screen()
            display_field(field, True)
            x, y = player_shot()
            result = check_shot(field, x, y)
            shots += 1

            if result == "Hit!" and all_ship_sunk(field):
                print("Congratulations! You won the game!")
                break
        replay = input("Do you want to play again? (yes or no): ")
        if replay == "no":
            print("Thanks you for playing")
            break

gameplay()
