from dataclasses import dataclass
from typing import Union


@dataclass
class Card:
    tag: int
    suit: int
    rank: int
    next: Union[str, int]

    def __str__(self):
        if self.tag == 1:
            return "Face Down"

        suit_table = {1: "Clubs", 2: "Diamonds", 3: "Hearts", 4: "Spades"}
        rank_table = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}
        rank_str = rank_table.get(self.rank) if rank_table.get(self.rank) else self.rank

        return f"{rank_str} of {suit_table[self.suit]}"
