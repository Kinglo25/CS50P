# Tic-Tac-Toe
#### Video Demo:  https://youtu.be/C5ifm2yCS8I
#### Description:
There will be two players in a game. Two signs represent each player. The general signs used in the game are X and O. Finally, there will be a board with 9 boxes.

The gameplay will be as follows.

 * First, one user will place their sign in one of the available empty boxes.
 * Next, the second user will place their sign in one of the available empty boxes.
 * The goal of the players is to place their respective signs completely row-wise or column-wise, or diagonally.
 * The game goes on until a player wins the game or it ended up in a draw by filling all boxes without a winning match.

 We will now discuss the algorithm to write the code. This algorithm will help you to write code in any programming language of your choice. Let’s see how it’s done.

# Create a board using a 2-dimensional array and initialize each element as empty.
You can represent empty using any symbol you like. Here, we are going to use a hyphen. '-'.

 # Write a function to check whether the board is filled or not.
Iterate over the board and return false if the board contains an empty sign or else return true.

# Write a function to check whether a player has won or not.
We have to check all the possibilities that we discussed in the previous section.
Check for all the rows, columns, and two diagonals.

# Write a function to show the board as we will show the board multiple times to the users while they are playing.

# Write a function to start the game.
* Select the first turn of the player randomly.
* Write an infinite loop that breaks when the game is over (either win or draw).
* Show the board to the user to select the spot for the next move.
* Ask the user to enter the row and column number.
* Update the spot with the respective player sign.
* Check whether the current player won the game or not.
* If the current player won the game, then print a winning message and break the infinite loop.
* Next, check whether the board is filled or not.
* If the board is filled, then print the draw message and break the infinite loop.
# Finally, show the user the final view of the board.
You may be able to visualize what’s happening. Don’t worry, even if you didn’t understand it completely. You will get more clarity once you see the code.

