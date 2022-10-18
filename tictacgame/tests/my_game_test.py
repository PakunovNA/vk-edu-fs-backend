"""Tic-tac-toe testing"""
from unittest import TestCase, main, mock
import io
import my_game


class TicTacGameTest(TestCase):
    """Class for tic-tac-toe testing"""

    def setUp(self):
        self.tic_tac_game = my_game.TicTacGame()

    def test_correct_input(self):
        """User entered the correct number"""
        self.assertEqual(self.tic_tac_game.validate_input("1"), True)

    def test_incorrect_type(self):
        """User entered not a number"""
        self.assertRaises(TypeError, self.tic_tac_game.validate_input, "some string")

    def test_incorrect_index(self):
        """User entered the number of a non-existent cell"""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.assertRaises(IndexError, self.tic_tac_game.validate_input, "0")
            self.assertRaises(IndexError, self.tic_tac_game.validate_input, "10")

    def test_incorrect_value(self):
        """User entered the number of the occupied cell"""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.tic_tac_game.cells[1] = 'X'
            self.assertRaises(ValueError, self.tic_tac_game.validate_input, "1")

    def test_check_winner(self):
        """Game ended with the user's win"""
        with mock.patch('sys.stdout', new=io.StringIO()):
            for i in range(1, 4):
                self.tic_tac_game.cells[i] = "X"
            self.assertEqual(self.tic_tac_game.check_winner("X"), True)
            for i in range(4, 7):
                self.tic_tac_game.cells[i] = "O"
            self.assertEqual(self.tic_tac_game.check_winner("O"), True)

    def test_check_tie(self):
        """The game ended in a tie"""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.tic_tac_game.cells = {1: "X", 2: "O", 3: "X",
                                       4: " ", 5: " ", 6: " ",
                                       7: " ", 8: " ", 9: " "}
            self.assertEqual(self.tic_tac_game.check_tie(), False)

            self.tic_tac_game.cells = {1: "X", 2: "O", 3: "X",
                                       4: "O", 5: "O", 6: "X",
                                       7: "X", 8: "X", 9: "O"}
            self.assertEqual(self.tic_tac_game.check_tie(), True)


if __name__ == '__main__':
    main()
