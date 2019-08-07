import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []

    def build_deck(self):
        suits = ['hearts', 'clubs', 'spades', 'diamonds']
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))
    def shuffle(self):
        random.shuffle(self.deck)
        return self 
    def deal(self, *player):
        self.shuffle()
        for p in player:
            for i in range(7):
                p.hand.append(self.deck.pop())
    def draw(self, player):
        player.hand.append(self.deck.pop())

class Player:
    def __init__(self, hand = [], name = '', pairs = 0):
        self.hand = hand
        self.name = name
        self.pairs = pairs
    def ask(self, player, target, card):
        for in target.hand:
            if i.values == card:
                player.hand.append(target.hand.pop(count))


player1 = Player(hand = [], name = 'p1', pairs = 0)
player2 = Player(hand = [], name = 'p2', pairs = 0)

d1 = Deck()
d1.build_deck()
print(d1.deck)
print(len(d1.deck))
    