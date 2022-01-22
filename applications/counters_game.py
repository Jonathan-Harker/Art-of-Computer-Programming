import math

from exercises.chapter_1.two.fibonacci_numbers import get_fibonacci_sequence


class CountersGame:
    def __init__(self, counters: int):
        self.counters = counters
        self.counters_taken_last_turn = counters

    def computer_move(self):
        max_move = min(math.ceil(self.counters / 3) - 1, 2*self.counters_taken_last_turn)
        min_counters_to_leave = self.counters - max_move
        fib_nums = get_fibonacci_sequence(limit=20)

        counters_to_leave = self.counters - 1
        for i in range(min_counters_to_leave, self.counters):
            if i in fib_nums:
                counters_to_leave = i
                break

        self.counters_taken_last_turn = self.counters - counters_to_leave
        self.counters = counters_to_leave
        print(f"AI: I have taken {self.counters_taken_last_turn} counters leaving {self.counters} for you")

    def player_move(self):
        self.counters_taken_last_turn = 2 * self.counters_taken_last_turn
        self.counters = self.counters - self.counters_taken_last_turn
        print(f"Predictable Player: I have taken {self.counters_taken_last_turn} counters leaving {self.counters} for you")


if __name__ == "__main__":
    game = CountersGame(counters=1000)
    while game.counters > 0:
        game.computer_move()
        game.player_move()
