"""
Homework number 1
Tic-tac-toe game.
"""


class TicTacGame:
    """Class of tic-tac-toe console game"""

    def __init__(self):
        self.cells = {1: " ", 2: " ", 3: " ",
                      4: " ", 5: " ", 6: " ",
                      7: " ", 8: " ", 9: " "}

    def show_board(self):
        """Output the game board to the console"""
        print("\nTic-tac-toe game board: ")
        for i in range(3):
            print(f" {self.cells[i * 3 + 1]} | {self.cells[i * 3 + 2]} | {self.cells[i * 3 + 3]} ")
            if i in range(2):
                print('-----------')

    def check_winner(self, player):
        """Checking the win of one of the players"""
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                      [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            win_condition = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    win_condition = False
            if not win_condition:
                continue
            self.show_board()
            print(f"Player {player} wins!")
            return True
        return False

    def check_tie(self):
        """Checking for a tie"""
        for i in range(1, 10):
            if self.cells[i] == " ":
                return False
        self.show_board()
        print("It's a tie game!")
        return True

    def select_cell(self, player):
        """Adding a value to a selected cell"""
        while True:
            try:
                print(f"Player {player}! Select cell number (1 - 9): ")
                selected_cell = input()
                flag = self.validate_input(selected_cell)
                self.cells[int(selected_cell)] = player
            except TypeError:
                print("Error! Please enter the number\n")
                continue
            except IndexError:
                print("Error! Enter a number in the range from 1 to 9\n")
                continue
            except ValueError:
                print("Error! This cell is already occupied, select another one\n")
                continue
            else:
                return flag

    def validate_input(self, inp):
        """User input validation"""
        if not inp.isdigit():
            raise TypeError
        if not 1 <= int(inp) <= 9:
            raise IndexError
        if self.cells[int(inp)] != " ":
            raise ValueError
        return True

    def start_game(self):
        """Game start point"""
        player = 'X'
        while True:
            self.show_board()
            self.select_cell(player)
            some_one_wins = self.check_winner(player)
            if some_one_wins:
                break
            tie_game = self.check_tie()
            if tie_game:
                break
            if player != "X":
                player = "X"
            else:
                player = "0"


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
