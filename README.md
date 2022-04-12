# This project is an assignment for the module "Open Source SW" from ChungAng University 
The goal of the first term-project is to implement asimple version of the game of “Snake”.

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
