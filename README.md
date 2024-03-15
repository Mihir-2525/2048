# 2048 Game

This is a Python implementation of the popular game 2048.

## How to Run

1. **Install Python**: If you haven't already installed Python, download and install it from the [official website](https://www.python.org/downloads/).
2. **Clone the Repository**: Clone this repository to your local machine using the following command: `git clone https://github.com/Mihir-2525/2048.git`
3. **Navigate to the Project Directory**: Open a terminal or command prompt and change to the directory where the repository was cloned.
4. **Run the Game**: Execute the following command to start the game:  `python 2048.py`

## Controls

- Use arrow keys (up, down, left, right) or `W`, `S`, `A`, `D` keys to move tiles.
- Press `X` key to exit the game.

## Difficulty Levels

- **High**: Tiles are mostly 2s with a 10% chance of a 4.
- **Medium**: Tiles are 2s with an 80% chance, 4s with a 15% chance, and occasionally 8s with a 5% chance.
- **Low**: Tiles are 2s with a 70% chance, 4s with a 23% chance, and occasionally 8s with a 7% chance.
- **2048**: Tiles are either 128, 256, or sometimes 512.

## Dependencies

- Python 3.x

## How to Play

The goal of the game is to reach the 2048 tile by sliding numbered tiles on a grid. When two tiles with the same number touch, they merge into one, with the value of the sum of the two tiles. After each move, a new tile randomly appears on the grid. The game ends when the player reaches the 2048 tile or when there are no more valid moves.

## High Score Tracking

The game tracks high scores for each difficulty level and stores them in an XLSX file named `data.xlsx`. The file contains the highest scores achieved for each difficulty level, allowing players to compete for the highest score.
