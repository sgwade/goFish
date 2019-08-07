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
    def display(self, deck):
        if len(self.hand) == 0:
            print("You have no cards! ...Drawing...")
            deck.draw(self)
        player_hand = '' 
        for i in self.hand:
            player_hand += str(i.value) + ' of ' + i.suit + ' | '
        print(player_hand)
        return self
    def ask(self, target, card, deck):
        if len(self.hand) == 0:
            deck.draw(self)
            return self
        count1 = 0
        card = int(card)
        current_card = 0
        print(card)
        for i in target.hand:
            d = int(i.value)
            if d == card:
                target.hand.pop(count1)
                self.pairs += 1
                for x in self.hand:
                    if x.value == card:
                        self.hand.pop(current_card)
                        print(f"You got a pair: {i} : {x}")
                        return self
                    current_card += 1
            count1 += 1
        deck.draw(self)
        print("Go fish!")
        return self
    def check_pairs(self):
        pass


def game_loop():
    d1 = Deck()
    d1.build_deck()
    player1 = Player(hand = [], name = 'p1', pairs = 0)
    player2 = Player(hand = [], name = 'p2', pairs = 0)
    d1.deal(player1, player2)
    player1.display(d1)
    player2.display(d1)
    player1.check_pairs()
    player2.check_pairs()
    current_player = player1
    while len(d1.deck) > 0:
        if current_player == player1:
            player1.check_pairs()
            player1.display(d1)
            current_ask = input("Player 1: what card are you looking for: ")
            player1.ask(player2, current_ask, d1)
            current_player = player2
        else:
            player2.check_pairs()
            player2.display(d1)
            current_ask = input("Player 2: What card are you looking for: ")
            player2.ask(player1, current_ask, d1)
            current_player = player1
    if player1.pairs > player2.pairs:
        print("Player 1 Wins!")
    elif player1.pairs < player2.pairs:
        print("Player 2 Wins!")
    else:
        print("It's a TIE!!!!")

game_loop()