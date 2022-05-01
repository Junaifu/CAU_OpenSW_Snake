# This project is an assignment for the module "Open Source SW" from ChungAng University 
The goal of the first term-project is to implement a simple version of the game of “Snake”.

## Notice
Programming language chosen: Python


## How to launch the project:
### Create virtual env
- Linux: ```virtualenv path/to/venv```
- Windows: ```python -m venv path/to/venv```

### Launch virtual env
- Linux: ```source venv/bin/activate```
- Windows: ```path/to/venv/Scripts/activate.ps1```
    (If ExecutionPolicy is restricted do this before: Set-ExecutionPolicy Unrestricted -Scope Process)

### Install dependencies in virtualenv
```
pip install -r requirements.txt
```
#### Launch the game
```
python snake/snake.py
```

## How to play the game:
### Game informations

The player controls the snake using arrow keys. The snake moves only north, south, east, or west, through respectively ``Up arrow key``, ``Down arrow key``, ``Right arrow key`` and ``Left arrow key``.
An apple appears at a random location, and when the snake "eats" (runs into) an apple, it gets longer. The number of apples eaten times 10 gives the final score.
The snake dies by either running into the edge of the board, or by running into
its own body.
The snake moves at a constant speed.

### Menus
#### Main menu

Also known as the starting screen.
You can choose between 4 buttons: PLAY, LOAD, RANKING and EXIT.
- PLAY starts a new game
- LOAD loads a saved game
- RANKING displays the top-ranked players’ name and score
- EXIT terminates the game

#### In-game menu

Also known as the pause screen.
To access the in-game menu, press the ``Esc`` (escape) key in the game.
You can then select between 4 buttons: RESUME, RESTART, SAVE and EXIT.
- RESUME continues to play the paused game
- RESTART starts a new game, instead of the paused game
- SAVE stores the current game status and returns to the main menu
- EXIT returns to the main menu without saving the current game status

### Backup file

Can be found in ``/backup_files`` directory.
Skeleton of a backup file:
```
sizeX,sizeY <-- (int, int) sizeX,sizeY are respectively the number of rows and columns of the map
Direction   <-- (from 1 to 4) direction of the snake (respectively North, South, East, West)
Score       <-- (int) score of the player
Map         <-- (row syntax: int, int, int .... int\n) map of the saved game
```
