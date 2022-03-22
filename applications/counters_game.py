import math
import random

from exercises.chapter_1.two.fibonacci_numbers import get_fibonacci_sequence
from utilities import get_sorted_list_neighbours


class CountersGame:
    def __init__(self, n: int):
        self.fib_nums = get_fibonacci_sequence(limit=20)
        self.n = n

    def computer_move(self, c: int, pm: int, t=0) -> int:
        if pm * 2 >= c and t == 0:
            self.n = 0
            return c

        c -= t
        max1 = math.ceil(c / 3) - 1
        max2 = 2 * pm
        max_move = min(max1, max2)

        if max_move < 2:
            self.n -= 1
            return 1

        min_cl = c - max_move

        if min_cl in fib_nums:
            self.n -= max_move
            return max_move

        pf, f = get_sorted_list_neighbours(l=self.fib_nums, i=min_cl)
        ai_move = c - f
        is_move_valid = max_move >= ai_move > 0

        if is_move_valid:
            self.n -= ai_move
            return ai_move

        t = pf
        return self.computer_move(c, pm, t)

    def player_move(self, pm: int):
        try:
            p_move = int(input("Your move: "))
        except ValueError:
            return self.player_move(pm=pm)

        if p_move > pm * 2 or p_move < 1:
            self.player_move(pm=pm)
        self.n -= p_move
        return p_move


if __name__ == "__main__":
    fib_nums = get_fibonacci_sequence(limit=20)
    n = random.randint(2, 5000)
    print(fib_nums)
    game = CountersGame(n=n)
    move = math.ceil(n/2) - 1
    turn = 1
    print(f"Game starting with {n} counters")
    while game.n > 0:
        if turn == 1 and n in fib_nums:
            move = game.player_move(pm=move)

        move = game.computer_move(c=game.n, pm=move)

        if game.n == 0:
            print(f"AI: I took {move} counters and left {game.n} so I win")
            exit(1)

        print(f"AI: I took {move} counters and left {game.n}")
        move = game.player_move(pm=move)
        print(f"Player: You took {move} counters and left {game.n}")
        turn += 1
