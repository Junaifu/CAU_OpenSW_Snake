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

There are 3 game modes : Single mode, Dual mode or Auto mode.

#### Single mode

The player controls the snake using arrow keys. The snake moves only north, south, east, or west, through respectively ``Up arrow key``, ``Down arrow key``, ``Right arrow key`` and ``Left arrow key``. An apple appears at a random location reachable by the snake.
When the snake "eats" (runs into) an apple, it gets longer. The number of apples eaten times 10 gives the final score.
The snake dies by either running into the edge of the board, or by running into its own body.
The snake moves at a constant speed.

#### Dual mode

Player 1 plays with w-a-s-d keys while Player 2 plays with the arrow keys. The snake moves only north, south, east, or west, through respectively ``W key``, ``S key``, ``D key`` and ``A key`` for Player 1 //``Up arrow key``, ``Down arrow key``, ``Right arrow key`` and ``Left arrow key`` for Player 2. Two apples are always displayed on the map, both reachable by the two snakes.
When the snake "eats" (runs into) an apple, it gets longer.
A snake dies by either running into the edge of the board, by running into its own body or by running into the other snake's body.
Both of the snakes move at a same constant speed.

#### Auto mode

Let the snake plays by itself. An apple appears at a random location reachable by the snake.
When the snake "eats" (runs into) an apple, it gets longer. The number of apples eaten times 10 gives the final score.
The snake dies by either running into the edge of the board, or by running into its own body.
The snake moves at a constant speed.

### Menus
#### Main menu

Also known as the starting screen.
You can choose between 6 buttons: SINGLE PLAY, DUAL PLAY, AUTO PLAY, LOAD, RANKING and EXIT.
- SINGLE PLAY starts a new single-player game
- DUAL PLAY starts a new dual-player game
- AUTO PLAY starts a new auto play game
- LOAD loads a saved single-player game
- RANKING displays the top-ranked players’ name and score
- EXIT terminates the game

#### In-game menu

Also known as the pause screen.
To access the in-game menu, press the ``Esc`` (escape) key in the game in any game mode.
You can then select between 4 buttons: RESUME, RESTART, SAVE (only available in Single Mode) and EXIT.
- RESUME continues to play the paused game
- RESTART starts a new game, instead of the paused game
- SAVE stores the current single-player game status and returns to the main menu
- EXIT returns to the main menu without saving the current game status

### Backup file

Can be found in ``/backup_files`` directory.
Skeleton of a backup file:
```
sizeX,sizeY     <-- (int, int) sizeX,sizeY are respectively the number of rows and columns of the map
Direction       <-- (from 1 to 4) direction of the snake (respectively North, South, East, West)
Snake coords    <-- [(int, int)] array of tuples of snake body's coords
Score           <-- (int) score of the player
Map             <-- (row syntax: int, int, int .... int\n) map of the saved game
```

### Score

For auto and single modes, the score will be displayed. For the dual mode, the winner will be shown.
