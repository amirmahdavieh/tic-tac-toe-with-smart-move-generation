# Tic-Tac-Toe AI with Smart Move Generation

This is a Python-based **Tic-Tac-Toe** game with a **Graphical User Interface (GUI)** built using `tkinter`. The computer opponent utilizes a smart move generation algorithm that prevents immediate threats and strategically places its moves to make the game more challenging.

## Features

- **Graphical Interface:** Play Tic-Tac-Toe using an interactive GUI.
- **AI Opponent:** The computer uses a strategy to block threats and make optimal moves.
- **Randomized Move Selection:** The AI selects moves using permutations and a predefined set of winning patterns.
- **Turn-Based Gameplay:** Human vs. Computer with alternating turns.

## How to Play

1. Start the game by running `tic_tac_toe.py`.
2. Click on an empty square to place an **X** (human player).
3. The computer will automatically place an **O** based on its move generation logic.
4. The game continues until there is a winner or the game results in a draw.

## Game Logic

- The computer uses the `generate_strings` function to analyze possible move sequences.
- It blocks threats when the human player is about to win.
- It strategically places its moves using a combination of predefined winning patterns.
- The game ends when there is a three-in-a-row match or all squares are filled.

## How the Computer Tries to Win

1. **Blocking Opponent's Winning Moves**: The AI first checks if the opponent (human) is one move away from winning and blocks that move.
2. **Winning When Possible**: If the AI itself is one move away from forming a three-in-a-row, it immediately plays that move to secure a win.
3. **Smart Move Generation**: The AI uses the `generate_strings` function to determine an optimal move sequence based on previously played moves.
4. **Strategic Positioning**: The AI prioritizes center and corner positions, as these give higher chances of forming winning combinations.
5. **Randomized Selection**: When multiple moves are equally good, the AI randomizes its choice to make gameplay less predictable.

