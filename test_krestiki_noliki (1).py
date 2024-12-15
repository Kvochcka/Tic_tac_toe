import mock
import pytest
from krestiki_noliki import KrestikiNoliki, repeat_play

class TestKrestikiNolikiCheckWinner:
    def test_check_winner_success(self):
        boards = [
            [
                ['X', 'X', 'X'],
                ['O', ' ', 'O'],
                ['O', ' ', 'X']
            ], [
                ['O', ' ', 'O'],
                ['X', 'X', 'X'],
                ['O', ' ', 'X']
            ], [
                ['O', ' ', 'O'],
                ['O', ' ', 'X'],
                ['X', 'X', 'X'],
            ], [
                ['X', 'O', 'X'],
                ['X', ' ', 'O'],
                ['X', ' ', 'O']
            ], [
                ['O', 'X', 'O'],
                ['X', 'X', ' '],
                ['O', 'X', ' ']
            ], [
                ['O', ' ', 'X'],
                ['O', ' ', 'X'],
                ['X', 'O', 'X'],
            ], [
                ['X', 'O', ' '],
                ['O', 'X', 'O'],
                ['X', ' ', 'X']
            ], [
                ['O', 'O', 'X'],
                ['X', 'X', ' '],
                ['X', 'O', ' ']
            ], [
                ['X', 'X', 'O'],
                ['X', 'O', ' '],
                ['O', 'O', 'X']
            ]
        ]

        for board in boards:
            game = KrestikiNoliki(board=board)
            game._current_player = int(not game._current_player)
            res = game._check_winner()
            assert res is True, f'{board=}, {game._current_player}'

    def test_check_winner_success_2(self):
        boards = [
            [
                ['X', 'X', 'X', 'X'],
                ['O', 'O', ' ', 'O'],
                ['O', ' ', 'X', ' '],
                ['O', ' ', ' ', 'X']
            ], [
                ['O', 'O', ' ', 'O'],
                ['X', 'X', 'X', 'X'],
                ['O', ' ', 'X', ' '],
                ['O', ' ', ' ', 'X']
            ], [
                ['O', 'O', ' ', 'O'],
                ['O', ' ', 'X', 'O'],
                ['X', 'X', 'X', 'X'],
                [' ', ' ', ' ', 'X']
            ], [
                ['X', 'O', 'X', 'X'],
                ['X', ' ', 'O', 'O'],
                ['X', ' ', ' ', ' '],
                ['X', ' ', 'O', ' ']
            ], [
                ['X', ' ', 'X', 'X'],
                [' ', 'X', ' ', 'X'],
                [' ', ' ', 'X', ' '],
                ['X', ' ', ' ', 'X']
            ], [
                ['X', ' ', ' ', 'X'],
                [' ', 'X', 'X', ' '],
                [' ', 'X', ' ', ' '],
                ['X', ' ', 'X', 'X']
            ]
        ]

        for board in boards:
            game = KrestikiNoliki(board=board, row_count=len(board), column_count=len(board[0]))
            game._current_player = int(not game._current_player)
            assert game._current_player == 0 # X, f'{board=}, {game._current_player}'
            res = game._check_winner()
            assert res is True, f'{board=}, {game._current_player}'

        boards = [
            [
                ['X', 'X', 'X', 'X', 'X'],
                ['O', 'O', ' ', 'O', ' '],
                ['O', ' ', 'X', 'O', ' '],
                ['O', ' ', ' ', 'X', ' '],
                [' ', ' ', ' ', ' ', 'X']
            ], [
                ['O', 'O', ' ', 'O', ' '],
                ['X', 'X', 'X', 'X', 'X'],
                ['O', ' ', 'X', 'O', ' '],
                ['O', ' ', ' ', 'X', ' '],
                [' ', ' ', ' ', ' ', 'X']
            ], [
                ['O', 'O', ' ', 'O', ' '],
                ['O', ' ', 'X', 'O', ' '],
                ['X', 'X', 'X', 'X', 'X'],
                ['O', ' ', ' ', 'X', ' '],
                [' ', ' ', ' ', ' ', 'X']
            ], [
                ['X', 'O', 'X', 'X', 'X'],
                ['X', ' ', 'O', 'O', 'X'],
                ['X', ' ', 'O', ' ', 'X'],
                ['X', ' ', 'O', ' ', 'X'],
                [' ', ' ', ' ', ' ', 'X']
            ], [
                ['X', ' ', 'X', 'X', 'X'],
                [' ', 'X', ' ', 'X', 'X'],
                [' ', ' ', 'X', ' ', 'X'],
                ['X', ' ', ' ', 'X', 'X'],
                [' ', ' ', ' ', ' ', 'X']
            ], [
                ['X', ' ', ' ', 'X', 'X'],
                [' ', 'X', 'X', ' ', 'X'],
                [' ', 'X', ' ', ' ', 'X'],
                ['X', ' ', 'X', 'X', 'X'],
                [' ', ' ', ' ', ' ', 'X']
            ]
        ]

        for board in boards:
            game = KrestikiNoliki(board=board, column_count=4, row_count=4)
            game._current_player = int(not game._current_player)
            assert game._current_player == 0, f'{board=}, {game._current_player}'  # X
            res = game._check_winner()
            assert res is True, f'{board=}, {game._current_player}'

    def test_check_winner_draw(self):
        boards = [
           [
                ['X', 'X', 'O', 'O'],
                ['O', 'O', 'X', 'X'],
                ['X', 'X', 'O', 'O'],
                ['O', 'O', 'X', 'X']
            ], [
                ['O', 'X', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['O', 'O', 'X', 'O'],
                ['X', 'O', 'X', 'O']
            ], [
                ['X', 'O', 'X', 'O', 'X'], #x= 13, o=12
                ['O', 'X', 'O', 'X', 'O'],
                ['O', 'X', 'O', 'X', 'O'],
                ['X', 'O', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'O', 'X']
            ], [
                ['O', 'X', 'O', 'X', 'O'], # x= 12, o=13
                ['X', 'O', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'O', 'X'],
                ['O', 'X', 'O', 'X', 'O'],
                ['O', 'X', 'O', 'X', 'O']
            ], [
                ['O', 'X', 'O'],
                ['O', 'X', 'X'],
                ['X', 'O', 'X']
            ]
        ]

        for board in boards:
            game = KrestikiNoliki(board=board)
            game._current_player = int(not game._current_player)
            res = game._check_winner()
            assert res is False, f'{board=}, {game._current_player}'


@pytest.fixture()
def game():
    return KrestikiNoliki()


class TestKresikiNolikiMove:
    @mock.patch('builtins.input', side_effect=['1,1'])
    def test_valid_move(self, mock_input, game):
        game._move()
        assert game._board[0][0] == 'X'

    # TODO читать о @mock.patch тут https://www.notion.so/mock-patch-603b2b974d39477bb3dd88e310983ad1

    @mock.patch('builtins.input', side_effect=['a,b', '2,2'])
    def test_invalid_format_then_valid_move_1(self, mock_input, game):
        with mock.patch('builtins.print') as mock_print:
            game._move()
            mock_print.assert_any_call('Invalid format. Please enter row and column numbers separated by a comma.')
        assert game._board[1][1] == 'X'

    @mock.patch('builtins.input', side_effect=['1,1', '1,1', '2,2'])
    def test_repeated_invalid_then_valid_move_2(self, mock_input, game):
        game._board[0][0] = 'X'
        with mock.patch('builtins.print') as mock_print:
            game._move()
            mock_print.assert_any_call('You cannot choose this cell, it is already filled.')
        assert game._board[1][1] == 'X'

    @mock.patch('builtins.input', side_effect=['4,5', '2,2'])
    def test_out_of_bounds_then_valid_move_3(self, mock_input, game):
        with mock.patch('builtins.print') as mock_print:
            game._move()
            mock_print.assert_any_call('Cell is out of bounds')
            mock_print.assert_any_call('Possible moves:', mock.ANY)
        assert game._board[1][1] == 'X'

    @mock.patch('builtins.input', side_effect=['-1,3', '2,2'])
    def test_out_of_bounds_then_valid_move_4(self, mock_input, game):
        with mock.patch('builtins.print') as mock_print:
            game._move()
            mock_print.assert_any_call('Cell is out of bounds')
            mock_print.assert_any_call('Possible moves:', mock.ANY)
        assert game._board[1][1] == 'X'

    @mock.patch('builtins.input', side_effect=['4.5', '2,2'])
    def test_out_of_bounds_then_valid_move_5(self, mock_input, game):
        with mock.patch('builtins.print') as mock_print:
            game._move()
            mock_print.assert_any_call('Invalid format. Please enter row and column numbers separated by a comma.')
        assert game._board[1][1] == 'X'

    def test_get_possible_moves(self):
        board = [
            ['X', 'O', 'X'],
            [' ', 'X', ' '],
            ['O', ' ', 'O']
        ]
        game = KrestikiNoliki()
        game._board = board
        expected_moves = [(2, 1), (2, 3), (3, 2)]
        assert game._get_possible_moves() == expected_moves

        board = [
            ['X', 'O', 'X', ' '],
            [' ', 'X', ' ', 'O'],
            ['O', ' ', 'O', ' '],
            [' ', 'X', ' ', ' ']
        ]
        game = KrestikiNoliki(row_count=4, column_count=4)
        game._board = board
        expected_moves = [(1, 4), (2, 1), (2, 3), (3, 2), (3, 4), (4, 1), (4, 3), (4, 4)]
        assert game._get_possible_moves() == expected_moves


class TestKrestikiNoliki:
    @mock.patch('builtins.input', side_effect=['2,2', '1,2', '3,3', '1,1', '1,3', '2,3', '3,1'])
    def test_game(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            game = KrestikiNoliki()
            game.play()
            mock_print.assert_any_call('X wins!')

    @mock.patch('builtins.input', side_effect=['2,2', '1,1', '3,3', '3,2', '3,1', '2,1', '1,2', '1,3', '2,3'])
    def test_game_draw(self, mock_input):
        """
          O  | X   |  O
        -----------------
          O  |  X  |  X
        -----------------
          X |  O  |  X
        """
        with mock.patch('builtins.print') as mock_print:
            game = KrestikiNoliki()
            game.play()
            mock_print.assert_any_call('Ничья!')

    @mock.patch('builtins.input', side_effect=['1,1', '2,2', '1,2', '2,3', '1,3', '3,3'])
    def test_game_4x4(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            game = KrestikiNoliki(row_count=4, column_count=4)
            game.play()
            mock_print.assert_any_call('X wins!')

    @mock.patch('builtins.input', side_effect=['1,1', '2,2', '1,2', '2,3', '1,3', '3,3', '1,4', '2,4', '1,5'])
    def test_game_5x5(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            game = KrestikiNoliki(row_count=5, column_count=5)
            game.play()
            mock_print.assert_any_call('X wins!')

class TestRepeatPlay:
    @mock.patch('builtins.input', side_effect=['y'])
    def test_repeat_play_yes(self, mock_input):
        result = repeat_play()
        assert result is True

    @mock.patch('builtins.input', side_effect=['n'])
    def test_repeat_play_no(self, mock_input):
        result = repeat_play()
        assert result is False

    @mock.patch('builtins.input', side_effect=['invalid', 'y'])
    def test_repeat_play_invalid_then_yes(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            result = repeat_play()
            mock_print.assert_any_call("Incorrect entry. Enter 'Y' to continue and 'N' to...none.")
        assert result is True

    @mock.patch('builtins.input', side_effect=['invalid', 'n'])
    def test_repeat_play_invalid_then_no(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            result = repeat_play()
            mock_print.assert_any_call("Incorrect entry. Enter 'Y' to continue and 'N' to...none.")
        assert result is False