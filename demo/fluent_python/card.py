import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    for i in range(3):
        print(choice(deck))

    # 下面列出了查看一摞牌最上面3张和只看牌面是 A 的牌的操作。
    print(deck[:3])

    # 先抽出索引是12的那张牌，然后每隔13张牌拿1张
    print(deck[12::13])

    # for card in deck:
    #     print(card)

    # for card in reversed(deck):
    #     print(card)

    for card in sorted(deck, key=spades_high, reverse=True):
        print(card)
