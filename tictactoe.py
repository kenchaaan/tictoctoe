# %%
from itertools import product


class Tictactoe:
    def __init__(self) -> None:
        self.board: dict = {(row, col): ' ' for row,
                            col in product(range(0, 3), range(0, 3))}

    def o_set(self, row: int, col: int) -> None:
        self.board[(row, col)] = 'o'

    def x_set(self, row: int, col: int) -> None:
        self.board[(row, col)] = 'x'

    def print(self) -> None:
        print('   0   1   2  ')
        print(' |---|---|---|')
        for row in range(0, 3):
            row_str = f'{row}|'
            for col in range(0, 3):
                row_str += f' {self.board[(row, col)]} '
                row_str += '|'
            print(row_str)
            print(' |---|---|---|')

    def is_finished(self):
        """board を見て、どちらが勝ったかを判定する

        どちらかが勝ってたら、勝っている方のシンボル 'x' か 'o' を返す。
        まだどちらも勝ってないなら None を返す。
        """
        def f(items):
            o_count = items.count('o')
            if o_count == 3:
                return 'o'
            x_count = items.count('x')
            if x_count == 3:
                return 'x'
            return None

        symbols = ['o', 'x']
        # 行ごとに見て、どちらかが勝ってる
        for row in range(0, 3):
            items = [self.board[(row, col)] for col in range(0, 3)]
            if r := f(items):
                return r
        for col in range(0, 3):
            items = [self.board[(row, col)] for row in range(0, 3)]
            if r := f(items):
                return r

        for a in [[0, 1, 2], [2, 1, 0]]:
            items = [self.board[(d, d)] for d in a]
            if r := f(items):
                return r

        return None

    def play_game(self) -> None:
        for n in range(0, 9):
            print('x の番です')
            x_input = [int(i) for i in input().split(' ')]
            self.x_set(x_input[0], x_input[1])
            self.print()
            if result := self.is_finished():
                print(f'{result} の勝ち')
                return result

            print(f'n is {n}')
            print('o の番です')
            o_input = [int(i) for i in input().split(' ')]
            self.o_set(o_input[0], o_input[1])
            self.print()
            if result := self.is_finished():
                print(f'{result} の勝ち')
                return result



if __name__ == '__main__':
    t = Tictactoe()
    t.print()
    t.play_game()

# %%
