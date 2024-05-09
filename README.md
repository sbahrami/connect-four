# Connect Four AI

This project implements an AI for the game Connect Four using the Minimax algorithm with different heuristic evaluation strategies. The AI players are capable of playing against each other or against a random move player.

## Modules

- `connect_four.py`: Contains the game logic and definitions for the `State`, `Game`, and `Player` classes.
- `minimax.py`: Contains the implementation of the Minimax algorithm and different heuristic functions.

## Players

- **MinimaxPlayer**: Uses the Minimax algorithm to determine the best move from a current game state.
- **RandomPlayer**: Selects moves randomly from the set of legal moves.
- **FirstMovePlayer**: Always selects the first legal move.
- **HumanPlayer**: Allows a human to play by selecting moves via keyboard input.

## Heuristic Functions

- **zero_heur**: Always returns 0 for non-terminal states; for terminal states, it returns 100, 0, or -100 based on whether the maximizer has won, the game is a draw, or the minimizer has won, respectively.
- **three_line_heur**: Evaluates states based on the number of three-in-a-row configurations for both players.
- **my_heuristic**: Evaluates states based on an advanced set of criteria, considering various patterns on the board.

## Usage

To use this AI, ensure that you have all the required modules and run the main script:

```bash
python minimax.py
