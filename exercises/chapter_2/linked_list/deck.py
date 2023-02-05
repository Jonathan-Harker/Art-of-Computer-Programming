import random
import uuid

from exercises.chapter_2.linked_list.card import Card


class Deck:
    def __init__(self):
        self.deck = {}
        self.top = None

    def set_ordered_deck(self):
        link = str(uuid.uuid4())
        for suit in range(1, 5):
            for rank in range(1, 14):
                next_link = self._set_link(rank, suit)
                self.deck[link] = Card(tag=1, suit=suit, rank=rank, next=next_link)
                self._set_top_card(link)
                link = next_link

    def shuffle(self):
        cards = []
        for card in self.deck:
            cards.append({"rank": self.deck[card].rank, "suit": self.deck[card].suit})

        random.shuffle(cards)

        for i, card in enumerate(self.deck):
            self.deck[card].rank = cards[i]["rank"]
            self.deck[card].suit = cards[i]["suit"]

    def _set_top_card(self, link: str):
        if not self.top:
            self.top = self.deck[link]

    @staticmethod
    def _set_link(rank: int, suit: int) -> str:
        next_link = str(uuid.uuid4())

        if suit == 4 and rank == 13:
            next_link = None

        return next_link


deck = Deck()
deck.set_ordered_deck()
top: Card = deck.top
top.tag = 0
# print(top)

while top.next:
    top = deck.deck[top.next]
    top.tag = 0
    # print(top)

deck.shuffle()
# print(top)

# for card in deck.deck:
#     print(deck.deck[card].next)
top = deck.top
print(top)
while top.next:
    top = deck.deck[top.next]
    print(top)
