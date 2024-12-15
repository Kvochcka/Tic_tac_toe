"""
* Для учителя
Условие задачи:
Сделать игру "крестики - нолики"
Результат ≈ ?%
Вердикт: ...
"""
class KrestikiNoliki:
    def __init__(self, row_count: int = 3, column_count: int = 3):
        # TODO заменить глобальные переменные на атриббуты объекта
        self.EMPTY_CELL = ' '
        self.row_count = row_count
        self.column_count = column_count
        self.board_row_last_index = row_count - 1
        self.board_column_last_index = column_count - 1

        self._board = self._init_board()
        self._players = ['X', 'O']
        self._current_player = 0
        self._step = 0

    def _init_board(self):
        return [
            [f'{i},{j}' for j in range(self.column_count)]
            for i in range(self.row_count)
        ]

    def play(self):
        print('Welcome to Tic-Tac-Toe!')
        print(
            'To make a move, enter the row and column numbers separated by a comma.\n'
            'For example, to place your mark in the center: 2, 2.'
        )
        self.print_board()

        last_step = self.row_count * self.column_count
        while True:
            self._move()
            self._step += 1
            self.print_board()

            if self._check_winner():
                print(f'{self._current_player} wins!')
                break
            elif self._step == last_step:
                print('Ничья!')
                break

            self._current_player = int(not self._current_player)

    def _move(self):
        while True:
            move = input(f'Player {self._players[self._current_player]}: ').split(',')
            try:
                row = int(move[0]) - 1
                col = int(move[1]) - 1
            except (ValueError, IndexError):
                print('Invalid format. Please enter row and column numbers separated by a comma.')
                print('Possible moves:', ' || '.join([f'{move[0]}, {move[1]}' for move in self._get_possible_moves()]))
                continue

            if row < 0 or row >= self.row_count or col < 0 or col >= self.column_count:
                print(f'Cell is out of bounds')
                print('Possible moves:', ' || '.join([f'{move[0]}, {move[1]}' for move in self._get_possible_moves()]))
                continue

            if not self._is_valid_move(row, col):
                print('You cannot choose this cell, it is already filled.')
                print('Possible moves:', ' || '.join([f'{move[0]}, {move[1]}' for move in self._get_possible_moves()]))
                continue

            self._board[row][col] = self._players[self._current_player]
            break

    def print_board(self):
        for i, row in enumerate(self._board):
            for j, cell in enumerate(row):
                print(f' {cell} ', end='\n' if j == self.board_column_last_index else '|')
            if i != self.board_row_last_index:
                print('-' * (6 * self.column_count - 1))

    def _is_valid_move(self, row, col):
        if (row < 0 or row >= len(self._board)) or (col < 0 or col >= len(self._board[0])):
            return False
        elif self._board[row][col] in self._players:
            return False
        return True

    def _get_possible_moves(self):
        possible_moves = []
        for i, row in enumerate(self._board):
            for j, cell in enumerate(row):
                if self._board[i][j] not in self._players:
                    possible_moves.append((i + 1, j + 1))
        return possible_moves

    def _check_winner(self):
        for i, row in enumerate(self._board):
            count_value = 0
            for j, cell in enumerate(row):
                if cell == self.current_player_sign:
                    count_value += 1
                else:
                    count_value = 0

                if count_value == 3:
                    return True

        for j in range(self.column_count):
            count_value = 0
            for i in range(self.row_count):
                cell = self._board[i][j]
                if cell == self.current_player_sign:
                    count_value += 1
                else:
                    count_value = 0

                if count_value == 3:
                    return True

        for i in range(self.row_count - 2):
            for j in range(self.column_count - 2):
                if self._board[i][j] == self._board[i + 1][j + 1] == self._board[i + 2][j + 2] == self.current_player_sign:
                    return True
                if self._board[i][j + 2] == self._board[i + 1][j + 1] == self._board[i + 2][j] == self.current_player_sign:
                    return True
        return False


def repeat_play():
    while True:
        user_input = input('Do you want to play again? Y/N: ').strip().lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        else:
            print("Incorrect entry. Enter 'Y' to continue and 'N' to...none.")


def main():
    while True:
        game = KrestikiNoliki()
        game.play()
        if not repeat_play():
            break

if __name__ == "__main__":
    main()

